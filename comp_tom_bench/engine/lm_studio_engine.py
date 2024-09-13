from openai import OpenAI
from comp_tom_bench.engine.inference_engine import InferenceEngine

class LMStudioInferenceEngine(InferenceEngine):
    """
    LM Studio inference engine.
    """
    def __init__(self, model_name: str):
        self.base_url = "http://localhost:1234/v1"
        self.model_name = model_name
        self.client = OpenAI(
            base_url=self.base_url,
            api_key="placeholder"
        )

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the LM Studio model.
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
