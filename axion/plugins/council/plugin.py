
from axion.core.plugins import AxionPlugin
from axion.models.base import get_model, AIModel
from axion.core.trace import get_current_trace
from typing import List, Dict, Any, Optional
import json

class CouncilPlugin(AxionPlugin):
    @property
    def name(self) -> str:
        return "council"

    @property
    def description(self) -> str:
        return "A multi-agent system for obtaining expert consensus on complex topics."

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "consult_council",
                "description": "Consult a panel of AI experts to get a consensus recommendation.",
                "parameters": {
                    "query": "string",
                    "num_experts": "integer",
                    "personas": "array",
                    "strategy": "string"
                },
                "func": self.consult_council
            }
        ]

    def consult_council(self, query: str, num_experts: int = 3, personas: List[str] = [], strategy: str = "consensus") -> str:
        """
        Orchestrates a council of experts to debate and reach a consensus.
        """
        trace = get_current_trace()
        if trace:
            trace.add_step("Council", f"Convening council for: {query[:50]}...", metadata={"strategy": strategy})

        model = get_model()
        
        # 1. Brainstorm Personas
        selected_personas = personas
        if not selected_personas:
            selected_personas = self._brainstorm_personas(model, query, num_experts)
            if trace:
                trace.add_step("Council", f"Selected personas: {', '.join(selected_personas)}")

        # 2. Expert Debate
        opinions = []
        for persona in selected_personas:
            opinion = self._get_expert_opinion(model, persona, query)
            opinions.append({"persona": persona, "opinion": opinion})
            if trace:
                trace.add_step("Council", f"Expert {persona} opined", details=opinion[:100] + "...")

        # 3. Judge Synthesis
        final_verdict = self._judge_synthesis(model, query, opinions)
        
        result = {
            "recommendation": final_verdict.get("recommendation", "No consensus reached"),
            "confidence": final_verdict.get("confidence", 0.0),
            "expert_opinions": opinions,
            "reasoning": final_verdict.get("reasoning", "")
        }
        
        if trace:
             trace.add_step("Council", "Consensus reached", details=result["reasoning"][:100] + "...")
             
        return json.dumps(result, indent=2)

    def _brainstorm_personas(self, model: AIModel, query: str, count: int) -> List[str]:
        prompt = (
            f"Identify {count} distinct professional personas strictly relevant to answering this query: '{query}'. "
            "Return ONLY a comma-separated list of roles (e.g. 'Security Engineer, DB Admin')."
        )
        response = model.chat([{"role": "user", "content": prompt}])
        # Cleanup response
        content = response.content.replace("Persons:", "").replace("Roles:", "").strip()
        personas = [p.strip() for p in content.split(",") if p.strip()]
        return personas[:count]

    def _get_expert_opinion(self, model: AIModel, persona: str, query: str) -> str:
        prompt = (
            f"You are a world-class {persona}. "
            f"Analyze the following query and provide your expert technical opinion: '{query}'. "
            "Be concise and focus on your domain of expertise."
        )
        response = model.chat([{"role": "user", "content": prompt}])
        return response.content

    def _judge_synthesis(self, model: AIModel, query: str, opinions: List[Dict[str, str]]) -> Dict[str, Any]:
        opinions_str = "\n\n".join([f"--- Expert: {o['persona']} ---\n{o['opinion']}" for o in opinions])
        
        prompt = (
            f"You are the Chief Technology Officer. Review the following expert opinions on the query: '{query}'.\n\n"
            f"{opinions_str}\n\n"
            "Synthesize a final recommendation. Return a JSON object with keys: "
            "'recommendation' (string), 'confidence' (float 0-1), 'reasoning' (string summary of why)."
            "Respond ONLY with the JSON."
        )
        
        response = model.chat([{"role": "user", "content": prompt}])
        content = response.content
        
        # Simple cleanup for markdown code blocks if the model adds them
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
            
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "recommendation": content,
                "confidence": 0.5,
                "reasoning": "Failed to parse Judge's JSON response."
            }
