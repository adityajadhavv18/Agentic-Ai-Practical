# Weather Agent

A small Python agent that fetches and displays weather information for a given location.

## Features

- Fetch current weather for a city
- Simple CLI example to demonstrate usage

## Requirements

- Python 3.8+
- Dependencies listed in the project's `requirements.txt`

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the agent with one of the entry scripts in this folder. Example:

```bash
python "weather agent/main.py"
# or
python "weather agent/agent.py"
```

Example output (depends on the implementation and API availability):

```
Fetching weather for London...
Temperature: 15°C
Condition: Light rain
```

## Files

- `agent.py` — core agent implementation
- `main.py` — example runner / CLI

## Contributing

Contributions and improvements are welcome. Open an issue or submit a PR.

## License

Choose a license for your project (e.g., MIT). Add a `LICENSE` file if needed.

## Contact

If you want help integrating this agent into a larger project, ask here or open an issue.
