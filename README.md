# Wikipedia Research Crew

Welcome to the DocsAgent Crew project, powered by [crewAI](https://crewai.com). This project is enhanced with a Wikipedia Research agent to extract and summarize information from Wikipedia.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [crewAI](https://crewai.com).

### 1. Environment Setup

To set up the virtual environment and install all required dependencies:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install crewAI CLI and sync project
pip install crewai
crewai install
```

### 2. Local LLM Setup (Ollama)

This project is configured to use a local LLM via [Ollama](https://ollama.com).

```bash
# Install Ollama via Homebrew
brew install ollama

# Start the Ollama background service
brew services start ollama

# Download the model
ollama pull llama3.1
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file** (Use `NA` if only using local Ollama)

- `src/docs_agent/config/agents.yaml`: Defines the agents.
- `src/docs_agent/config/tasks.yaml`: Defines the tasks.
- `src/docs_agent/crew.py`: Contains the crew logic, tools, and LLM configuration.
- `src/docs_agent/tools/wikipedia_tool.py`: The custom Wikipedia search tool.

## Running the Project

To kickstart your crew of AI agents:

1. **Verify Ollama is active**: Ensure [http://localhost:11434](http://localhost:11434) is accessible.
2. **Run the Crew**:
```bash
crewai run
```
3. **Provide a Prompt**: The terminal will ask you: *"What topic would you like the agents to research today?"*. Type your topic (e.g., "History of Apple Inc") and press Enter.

The final result will be saved in `report.md`.

### Sample Output
When searching for "List of Presidents of the United States by time in office", you can expect an output like this:

```markdown
| Rank | President | Number of Days | Years |
| --- | --- | --- | --- |
| 1 | Franklin D. Roosevelt | 4,422 days | 12 years (1933-1945) |
| 2 | William Henry Harrison | 1 day | <1 year (1841) |
| 3 | James A. Garfield | 199 days | <1 year (1881) |
| 4 | Warren G. Harding | 881 days | 2 years, 7 months (1921-1923) |
| ... | ... | ... | ... |
```

> **Note**: The program is designed to perform a specific task and then exit. Once the "Crew Execution Completed" message appears and the final output is shown, the script finishes its job and returns you to the terminal prompt.



## Cleanup

To stop the background services and uninstall Ollama when finished:

```bash
# Stop the Ollama background service
brew services stop ollama

# Uninstall Ollama
brew uninstall ollama

# (Optional) Remove downloaded models
rm -rf ~/.ollama
```

## Troubleshooting

### 1. Connection Refused (Ollama)
If you see `litellm.exceptions.APIConnectionError: OllamaException - [Errno 61] Connection refused`:
* **Check if Ollama is running**: Run `curl http://localhost:11434`. It should say "Ollama is running".
* **Manual Start**: If it's not running, start it manually with `ollama serve`.

### 2. Missing Dependencies (apscheduler/email-validator/fastapi-sso)
If you see `ImportError: Missing dependency No module named 'apscheduler'`, `ImportError: email-validator is not installed`, or `ModuleNotFoundError: No module named 'fastapi_sso'`:
* These are internal requirements for certain `litellm` and `pydantic` features. 
* **Fix**: Run `crewai install` again to sync the updated dependencies from `pyproject.toml`.



### 3. Stuck Processes/Venv Confusion
If the environment feels stuck or you've made changes to the venv:
```bash
# Deactivate current session
deactivate

# Re-activate
source .venv/bin/activate

# Run the crew
crewai run
```


## Understanding Your Crew

The **DocsAgent Crew** now includes:
- **Wikipedia Information Extractor**: Specialized in searching and summarizing Wikipedia articles.


## Support

For support, questions, or feedback regarding the DocsAgent Crew or crewAI.
- Visit the [documentation](https://docs.crewai.com)
- Reach out to the [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Chat with the docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


