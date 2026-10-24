The Problem: Incompatible LLM API Proxies/Providers

Developers in the agentic AI community frequently encounter issues with LLM API compatibility when using different providers (e.g., OpenAI, Anthropic, Google) or proxy services (e.g., OpenRouter, LiteLLM). These services often have subtle differences in their request/response schemas, error handling, and streaming protocols. This leads to unexpected behavior, errors, and significant development overhead when trying to integrate various LLMs or switch between proxy services for cost optimization, reliability, or specific model access. The core issue is the lack of a standardized, robust, and easily adaptable interface for interacting with diverse LLM endpoints.

Why this project shape/stack was chosen:

This prototype is a lightweight Python library providing a **universal LLM client adapter**. Python is the de-facto language for agentic AI development, making a library the most accessible and deployable format. We've chosen a clear adapter pattern with a `BaseLLMClient` and concrete implementations for different providers/proxies. This allows developers to write their agent logic against a consistent interface, abstracting away the underlying LLM API specifics. The `httpx` library is used for robust, asynchronous HTTP requests, suitable for modern LLM interactions.

Setup and usage instructions (zero API keys):

1.  **Save the files:** Create a directory (e.g., `llm_client_adapter`) and save all the provided files into it.
2.  **Install dependencies:**
    ```bash
    pip install httpx
    ```
3.  **Run the example:**
    ```bash
    python main.py
    ```
    This will demonstrate interaction with the mock `OpenRouterClient` and `LiteLLMClient` using fixture data, showing how the unified interface works without needing any API keys or live network calls.

Optional real-LLM adapter:

This prototype includes an optional adapter for Google Gemini (via the `google-genai` SDK). To enable it:

1.  **Install the SDK:**
    ```bash
    pip install google-generativeai
    ```
2.  **Set your API key:**
    ```bash
    export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```
3.  **Uncomment the `GeminiClient` instantiation and usage in `main.py`**. The `main.py` currently focuses on the mock clients for zero-key demonstration, but the `GeminiClient` is fully implemented and ready to use.
