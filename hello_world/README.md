# hello_world

This folder contains two simple Python examples for getting started with generative AI:

- `googlegenai.py` - uses the Google Gemini API via the `google-genai` client.
- `main.py` - uses the OpenAI Python client with configuration loaded from a `.env` file.

## Setup

1. Create and activate a Python virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Configure credentials.

- For `main.py`, add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

- For `googlegenai.py`, replace the hard-coded `api_key` value with your Google API key or use a safer environment-based approach.

> Do not commit API keys or secrets to source control.

## Running the examples

- Run the OpenAI example:

```bash
python hello_world/main.py
```

- Run the Google Gemini example:

```bash
python hello_world/googlegenai.py
```

## Notes

- `main.py` sends a math-specific prompt to the OpenAI chat completion endpoint.
- `googlegenai.py` generates content from the Gemini model `gemini-2.5-flash`.
- Keep your API keys private and avoid sharing them.
