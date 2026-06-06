from config import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

class LLM:
    """
    A class to manage and provide access to the Gemini language model.
    """
    def __init__(self, model_name: str = "gemini-3.1-flash-lite", max_tokens: int = 2048, temperature: float = 0.5):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.api_key = GEMINI_API_KEY
        
        # Initialize the model instance
        self._model = ChatGoogleGenerativeAI(
            model=self.model_name,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            api_key=self.api_key
        )

    def get_model(self) -> ChatGoogleGenerativeAI:
        """
        Returns the configured ChatGoogleGenerativeAI instance.
        """
        return self._model

# You can still create a default instance here if you want it easily accessible,
# or you can instantiate the class wherever it's needed in your other files.
# gemini_instance = LLM().get_model()
