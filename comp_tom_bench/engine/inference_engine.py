from abc import ABC, abstractmethod

class InferenceEngine(ABC):
    """
    Abstract class for an LLM inference engine/provider.
    """
    @abstractmethod
    def generate_response(self, prompt):
        pass