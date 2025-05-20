# Introduction
This is a simple RAG application using Langchain with a simple CLI interface for answering questions related to a local document that is stored in the data/example.pdf

This app uses Ollama with the default LLM model being deepseek-r1:8b.

## Build Docker and run docker images
```bash
docker compose up -d
```

## Workaround for CLI input
Because docker compose up is incompatible with this app's CLI, a workaround is needed to allow for the user inputs.
```bash
docker attach file-qa-bot
```

After attaching to the Docker container, the app must be run:
```bash
python app.py
```

Now it should be possible to use the CLI interface normally.

To exit the app, simply write exit in the CLI.

## Shutting down containers
After usage, it is good practice to close the docker containers:
```bash
docker compose down
```