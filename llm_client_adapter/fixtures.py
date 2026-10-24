# --- Fixture data for OpenRouter ---
OPENROUTER_CHAT_COMPLETION_FIXTURE = {
    "id": "chatcmpl-mock-openrouter-12345",
    "object": "chat.completion",
    "created": 1701198751,
    "model": "mistralai/mistral-7b-instruct",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello! I am a mock assistant from OpenRouter."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 12,
        "total_tokens": 22
    }
}

OPENROUTER_STREAM_CHUNK_FIXTURE = [
    {
        "id": "chatcmpl-mock-stream-openrouter-1",
        "object": "chat.completion.chunk",
        "created": 1701198751,
        "model": "mistralai/mistral-7b-instruct",
        "choices": [
            {
                "index": 0,
                "delta": {"role": "assistant", "content": "This is "},
                "finish_reason": None
            }
        ]
    },
    {
        "id": "chatcmpl-mock-stream-openrouter-2",
        "object": "chat.completion.chunk",
        "created": 1701198752,
        "model": "mistralai/mistral-7b-instruct",
        "choices": [
            {
                "index": 0,
                "delta": {"content": "a streamed "},
                "finish_reason": None
            }
        ]
    },
    {
        "id": "chatcmpl-mock-stream-openrouter-3",
        "object": "chat.completion.chunk",
        "created": 1701198753,
        "model": "mistralai/mistral-7b-instruct",
        "choices": [
            {
                "index": 0,
                "delta": {"content": "response from OpenRouter."},
                "finish_reason": None
            }
        ]
    },
    {
        "id": "chatcmpl-mock-stream-openrouter-4",
        "object": "chat.completion.chunk",
        "created": 1701198754,
        "model": "mistralai/mistral-7b-instruct",
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop"
            }
        ]
    }
]

# --- Fixture data for LiteLLM (mimicking OpenAI format) ---
LITELLM_CHAT_COMPLETION_FIXTURE = {
    "id": "chatcmpl-mock-litellm-67890",
    "object": "chat.completion",
    "created": 1701198800,
    "model": "gpt-3.5-turbo",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Greetings from a mock LiteLLM proxy!"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 11,
        "completion_tokens": 10,
        "total_tokens": 21
    }
}

LITELLM_STREAM_CHUNK_FIXTURE = [
    {
        "id": "chatcmpl-mock-stream-litellm-1",
        "object": "chat.completion.chunk",
        "created": 1701198800,
        "model": "gpt-3.5-turbo",
        "choices": [
            {
                "index": 0,
                "delta": {"role": "assistant", "content": "This is "},
                "finish_reason": None
            }
        ]
    },
    {
        "id": "chatcmpl-mock-stream-litellm-2",
        "object": "chat.completion.chunk",
        "created": 1701198801,
        "model": "gpt-3.5-turbo",
        "choices": [
            {
                "index": 0,
                "delta": {"content": "a streamed "},
                "finish_reason": None
            }
        ]
    },
    {
        "id": "chatcmpl-mock-stream-litellm-3",
        "object": "chat.completion.chunk",
        "created": 1701198802,
        "model": "gpt-3.5-turbo",
        "choices": [
            {
                "index": 0,
                "delta": {"content": "response from LiteLLM."},
                "finish_reason": None
            }
        ]
    },
    {
        "id": "chatcmpl-mock-stream-litellm-4",
        "object": "chat.completion.chunk",
        "created": 1701198803,
        "model": "gpt-3.5-turbo",
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop"
            }
        ]
    }
]
