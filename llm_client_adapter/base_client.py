import abc
from typing import Dict, Any, AsyncIterator

class BaseLLMClient(abc.ABC):
    """
    Abstract base class for a universal LLM client.
    Defines a consistent interface for interacting with various LLM providers/proxies.
    """

    @abc.abstractmethod
    async def chat_completion(self, messages: list[dict], model: str, **kwargs) -> Dict[str, Any]:
        """
        Sends a chat completion request to the LLM.

        Args:
            messages: A list of message dictionaries (e.g., [{"role": "user", "content": "Hello"}]).
            model: The name of the model to use (e.g., "gpt-3.5-turbo", "gemini-pro").
            **kwargs: Additional parameters specific to the provider or common LLM features
                      (e.g., temperature, max_tokens, stream).

        Returns:
            A dictionary representing the LLM's response.
        """
        pass

    @abc.abstractmethod
    async def stream_chat_completion(self, messages: list[dict], model: str, **kwargs) -> AsyncIterator[Dict[str, Any]]:
        """
        Sends a streaming chat completion request to the LLM.

        Args:
            messages: A list of message dictionaries.
            model: The name of the model to use.
            **kwargs: Additional parameters.

        Returns:
            An async iterator yielding dictionaries representing chunks of the LLM's response.
        """
        pass

    @abc.abstractmethod
    def _parse_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Internal method to normalize a provider-specific response into a common format.
        """
        pass

    @abc.abstractmethod
    def _parse_stream_chunk(self, chunk: Dict[str, Any]) -> Dict[str, Any]:
        """
        Internal method to normalize a provider-specific stream chunk into a common format.
        """
        pass
