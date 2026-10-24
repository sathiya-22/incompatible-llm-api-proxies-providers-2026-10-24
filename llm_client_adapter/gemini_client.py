import os
from typing import Dict, Any, AsyncIterator
from .base_client import BaseLLMClient

try:
    import google.generativeai as genai
    from google.generativeai.types import GenerationConfig, StopCandidateException
    _GEMINI_AVAILABLE = True
except ImportError:
    _GEMINI_AVAILABLE = False
    print("Warning: google-generativeai not installed. GeminiClient will not function.")

class GeminiClient(BaseLLMClient):
    """
    Client for Google Gemini API.
    This requires the 'google-generativeai' package and GEMINI_API_KEY environment variable.
    """
    def __init__(self, api_key: str = None):
        if not _GEMINI_AVAILABLE:
            raise RuntimeError("google-generativeai package is not installed. Cannot use GeminiClient.")
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY must be provided or set as an environment variable.")
        genai.configure(api_key=self.api_key)

    def _convert_messages_to_gemini_format(self, messages: list[dict]) -> list[dict]:
        """Converts standard message format to Gemini's format."""
        gemini_messages = []
        for msg in messages:
            role = "user" if msg["role"] == "user" else "model"
            gemini_messages.append({"role": role, "parts": [{"text": msg["content"]}]})
        return gemini_messages

    async def chat_completion(self, messages: list[dict], model: str = "gemini-pro", **kwargs) -> Dict[str, Any]:
        print(f"[GeminiClient] Calling real Gemini API for model: {model}")
        gemini_messages = self._convert_messages_to_gemini_format(messages)
        generation_config = GenerationConfig(
            temperature=kwargs.get("temperature", 0.7),
            max_output_tokens=kwargs.get("max_tokens", None),
            stop_sequences=kwargs.get("stop", None)
        )
        try:
            model_instance = genai.GenerativeModel(model_name=model)
            response = await model_instance.generate_content_async(
                contents=gemini_messages,
                generation_config=generation_config
            )
            return self._parse_response(response)
        except StopCandidateException as e:
            # Handle cases where Gemini stops due to safety or other reasons
            print(f"Gemini stopped due to: {e.candidate.finish_reason}")
            return self._parse_response({"text": "", "finish_reason": e.candidate.finish_reason})
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            raise

    async def stream_chat_completion(self, messages: list[dict], model: str = "gemini-pro", **kwargs) -> AsyncIterator[Dict[str, Any]]:
        print(f"[GeminiClient] Streaming real Gemini API for model: {model}")
        gemini_messages = self._convert_messages_to_gemini_format(messages)
        generation_config = GenerationConfig(
            temperature=kwargs.get("temperature", 0.7),
            max_output_tokens=kwargs.get("max_tokens", None),
            stop_sequences=kwargs.get("stop", None)
        )
        try:
            model_instance = genai.GenerativeModel(model_name=model)
            response_stream = await model_instance.generate_content_async(
                contents=gemini_messages,
                generation_config=generation_config,
                stream=True
            )
            async for chunk in response_stream:
                yield self._parse_stream_chunk(chunk)
        except StopCandidateException as e:
            print(f"Gemini stopped due to: {e.candidate.finish_reason}")
            yield {"content": "", "finish_reason": e.candidate.finish_reason}
        except Exception as e:
            print(f"Error streaming Gemini API: {e}")
            raise

    def _parse_response(self, response: Any) -> Dict[str, Any]:
        """
        Normalizes Gemini's response format.
        """
        text_content = ""
        finish_reason = None
        if hasattr(response, 'text'):
            text_content = response.text
        elif isinstance(response, dict) and "text" in response: # For StopCandidateException handling
            text_content = response["text"]

        if hasattr(response, 'candidates') and response.candidates:
            if hasattr(response.candidates[0], 'finish_reason'):
                finish_reason = str(response.candidates[0].finish_reason).split('.')[-1].lower() # e.g., "STOP"
            # Add more parsing for safety ratings, etc., if needed

        return {
            "role": "assistant",
            "content": text_content,
            "finish_reason": finish_reason,
            "model": "gemini-pro", # Or parse from response if available
            "usage": {}, # Gemini API doesn't always return explicit token usage in the same way
            "raw_response": response
        }

    def _parse_stream_chunk(self, chunk: Any) -> Dict[str, Any]:
        """
        Normalizes Gemini's stream chunk format.
        """
        text_content = ""
        finish_reason = None
        if hasattr(chunk, 'text'):
            text_content = chunk.text

        if hasattr(chunk, 'candidates') and chunk.candidates:
            if hasattr(chunk.candidates[0], 'finish_reason'):
                finish_reason = str(chunk.candidates[0].finish_reason).split('.')[-1].lower()

        return {
            "content": text_content,
            "finish_reason": finish_reason,
            "raw_chunk": chunk
        }
