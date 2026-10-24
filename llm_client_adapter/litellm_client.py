import httpx
import json
from typing import Dict, Any, AsyncIterator
from .base_client import BaseLLMClient
from .fixtures import LITELLM_CHAT_COMPLETION_FIXTURE, LITELLM_STREAM_CHUNK_FIXTURE

class LiteLLMClient(BaseLLMClient):
    """
    Client for LiteLLM proxy API.
    This implementation uses fixture data for demonstration without API keys.
    """
    def __init__(self, api_key: str = "sk-LITELLM_MOCK_KEY", base_url: str = "http://localhost:4000"):
        self.api_key = api_key
        self.base_url = base_url # Default LiteLLM proxy URL
        self.client = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {self.api_key}"}
        )

    async def chat_completion(self, messages: list[dict], model: str, **kwargs) -> Dict[str, Any]:
        # For demonstration, return fixture data directly
        print(f"[LiteLLMClient] Simulating chat completion for model: {model}")
        return self._parse_response(LITELLM_CHAT_COMPLETION_FIXTURE)

    async def stream_chat_completion(self, messages: list[dict], model: str, **kwargs) -> AsyncIterator[Dict[str, Any]]:
        print(f"[LiteLLMClient] Simulating streaming chat completion for model: {model}")
        for chunk in LITELLM_STREAM_CHUNK_FIXTURE:
            yield self._parse_stream_chunk(chunk)
        # In a real implementation:
        # async with self.client.stream("POST", f"{self.base_url}/chat/completions",
        #                                json={"model": model, "messages": messages, "stream": True, **kwargs}) as response:
        #     response.raise_for_status()
        #     async for chunk_bytes in response.aiter_bytes():
        #         for line in chunk_bytes.decode('utf-8').split('\n'):
        #             if line.startswith('data: '):
        #                 try:
        #                     data = json.loads(line[len('data: '):])
        #                     yield self._parse_stream_chunk(data)
        #                 except json.JSONDecodeError:
        #                     continue

    def _parse_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalizes LiteLLM's (which often mimics OpenAI's) chat completion response format.
        """
        if not response or "choices" not in response or not response["choices"]:
            return {"role": "assistant", "content": ""}

        choice = response["choices"][0]
        message = choice.get("message", {})
        return {
            "role": message.get("role", "assistant"),
            "content": message.get("content", ""),
            "finish_reason": choice.get("finish_reason"),
            "model": response.get("model"),
            "usage": response.get("usage", {}),
            "raw_response": response
        }

    def _parse_stream_chunk(self, chunk: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalizes LiteLLM's (OpenAI-like) stream chunk format.
        """
        if not chunk or "choices" not in chunk or not chunk["choices"]:
            return {"content": "", "finish_reason": None}

        choice = chunk["choices"][0]
        delta = choice.get("delta", {})
        return {
            "content": delta.get("content", ""),
            "finish_reason": choice.get("finish_reason"),
            "raw_chunk": chunk
        }
