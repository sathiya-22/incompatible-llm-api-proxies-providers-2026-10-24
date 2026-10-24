import asyncio
from llm_client_adapter.openrouter_client import OpenRouterClient
from llm_client_adapter.litellm_client import LiteLLMClient
from llm_client_adapter.gemini_client import GeminiClient
import os

async def main():
    user_messages = [{"role": "user", "content": "Tell me a short story."}]

    print("--- Testing OpenRouterClient (Mock) ---")
    openrouter_client = OpenRouterClient()
    response = await openrouter_client.chat_completion(user_messages, model="mistralai/mistral-7b-instruct")
    print(f"OpenRouter Completion: {response['content']}")

    print("\n--- Testing OpenRouterClient Streaming (Mock) ---")
    async for chunk in openrouter_client.stream_chat_completion(user_messages, model="mistralai/mistral-7b-instruct"):
        print(f"OpenRouter Stream Chunk: {chunk['content']}", end="", flush=True)
    print("\n")

    print("\n--- Testing LiteLLMClient (Mock) ---")
    litellm_client = LiteLLMClient()
    response = await litellm_client.chat_completion(user_messages, model="gpt-3.5-turbo")
    print(f"LiteLLM Completion: {response['content']}")

    print("\n--- Testing LiteLLMClient Streaming (Mock) ---")
    async for chunk in litellm_client.stream_chat_completion(user_messages, model="gpt-3.5-turbo"):
        print(f"LiteLLM Stream Chunk: {chunk['content']}", end="", flush=True)
    print("\n")

    # --- Optional: Test GeminiClient if API key is set ---
    # To enable:
    # 1. pip install google-generativeai
    # 2. export GEMINI_API_KEY="YOUR_API_KEY"
    # 3. Uncomment the section below
    if os.getenv("GEMINI_API_KEY"):
        try:
            print("\n--- Testing GeminiClient (Real API) ---")
            gemini_client = GeminiClient()
            gemini_response = await gemini_client.chat_completion(user_messages, model="gemini-pro")
            print(f"Gemini Completion: {gemini_response['content']}")

            print("\n--- Testing GeminiClient Streaming (Real API) ---")
            async for chunk in gemini_client.stream_chat_completion(user_messages, model="gemini-pro"):
                print(f"Gemini Stream Chunk: {chunk['content']}", end="", flush=True)
            print("\n")
        except Exception as e:
            print(f"\nCould not initialize or use GeminiClient: {e}")
            print("Ensure 'google-generativeai' is installed and GEMINI_API_KEY is set correctly.")
    else:
        print("\nSkipping GeminiClient test. Set GEMINI_API_KEY environment variable to enable.")


if __name__ == "__main__":
    asyncio.run(main())
