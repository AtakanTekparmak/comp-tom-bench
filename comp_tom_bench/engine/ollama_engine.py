import ollama
from comp_tom_bench.engine.inference_engine import InferenceEngine

class OllamaInferenceEngine(InferenceEngine):
    """
    Ollama inference engine.
    """
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_response(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']