# Setting Up the Environment and Installing Dependencies

## For Mac/Linux/WSL:

1. **Create the environment and activate it:**
    ```bash
    python3 -m venv medical-doctor-assistant-env
    source medical-doctor-assistant-env/bin/activate
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Setting Up API Keys

### OpenAI API Key
1. If you don't have an OpenAI API key yet, you can sign up [here](https://openai.com/index/openai-api/).
2. Set your `OPENAI_API_KEY` in your environment variables.

### LangSmith API Key
1. Sign up for LangSmith [here](https://smith.langchain.com/).
2. Learn more about LangSmith and how to use it within your workflow [here](https://www.langchain.com/langsmith), and check out the relevant library [documentation](https://docs.smith.langchain.com/).
3. Set the following environment variables:
    ```bash
    LANGCHAIN_API_KEY=<your-api-key>
    LANGCHAIN_TRACING_V2=true
    ```

## Upgrade pip (optional)
To ensure you're using the latest version of `pip`, run:
```bash
pip install --upgrade pip
```

