# LangChain Learning

This repository is a hands-on collection of LangChain examples covering core concepts such as LLMs, chat models, embeddings, prompts, output parsing, structured outputs, chains, and runnable components.

The project is designed for learning and experimentation, with each folder focused on a specific LangChain capability.

## Project structure

- `01_LLMs/` - Basic LLM usage and integrations
- `02_ChatModels/` - Chat model examples for Anthropic, Google, Hugging Face, and OpenAI
- `03_Embeddings/` - Embedding generation and similarity examples
- `04_Prompts/` - Prompt templates and UI-driven prompt generation
- `05_OutputParsers/` - Parsing raw model output into JSON, strings, or structured data
- `06_StructuredOutput/` - Pydantic and TypedDict-based structured output demos
- `07_Chains/` - Sequential, parallel, conditional, and simple chain examples
- `08_Runnables/` - Runnable interfaces, composition patterns, and execution flow examples
- `chatbot.py` - Simple interactive chatbot example using Hugging Face
- `requirements.txt` - Python dependencies for the project

## Prerequisites

- Python 3.10 or newer
- A virtual environment (recommended)
- API keys for the providers you want to test (OpenAI, Anthropic, Google, Hugging Face, etc.)

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```powershell
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables in a `.env` file if needed:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

## Notes
- This is a learning repository, so examples may depend on third-party model APIs and may require valid credentials.
- Some scripts are intentionally simple and meant to illustrate LangChain concepts rather than production-ready architecture.
- If a model provider is not configured, skip that example or add the corresponding API key to your environment.
