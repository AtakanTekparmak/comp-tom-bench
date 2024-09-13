from openai import OpenAI
from comp_tom_bench.engine.inference_engine import InferenceEngine

class OpenAIInferenceEngine(InferenceEngine):
    """
    OpenAI inference engine.
    """
    def __init__(self, api_key: str, model_name: str = 'gpt-3.5-turbo'):
        self.api_key = api_key
        self.model_name = model_name
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=self.api_key,
        )

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You must strictly follow the user's instructions and output format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,    
            max_tokens=150,
        )
        return response.choices[0].message.content