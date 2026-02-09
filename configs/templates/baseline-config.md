# Baseline Configuration (2026-02-09)

| Parameter | Current Value | Default Value | Description |
|-----------|--------------|---------------|-------------|
| chat_model_provider | "openrouter" | openrouter | Provider for main chat model |
| chat_model_name | "openai/gpt-4.1" | openai/gpt-4.1 | Model name for chat |
| chat_model_kwargs | {"temperature": "0"} | {} | Extra kwargs for chat model |
| util_model_provider | "openrouter" | openrouter | Provider for utility model |
| util_model_name | "openai/gpt-4.1-mini" | openai/gpt-4.1-mini | Model name for utility tasks |
| util_model_kwargs | {"temperature": "0"} | {} | Extra kwargs for utility model |
| embed_model_provider | "huggingface" | huggingface | Provider for embedding model |
| embed_model_name | "sentence-transformers/all-MiniLM-L6-v2" | sentence-transformers/all-MiniLM-L6-v2 | Embedding model name |
| embed_model_kwargs | {} | {} | Extra kwargs for embedding model |
| browser_model_provider | "openrouter" | openrouter | Provider for browser agent model |
| browser_model_name | "openai/gpt-4.1" | openai/gpt-4.1 | Model name for browser agent |
| browser_model_kwargs | {"temperature": "0"} | {} | Extra kwargs for browser model |
| version | v0.9.7-10 | v0.9.7-10 | Agent Zero version |