# RAG Queue

A small retrieval-augmented generation (RAG) queue service built with FastAPI, Redis Queue (RQ), Qdrant, and OpenAI.

## Overview

This module exposes a `/chat` endpoint that enqueues user queries into Redis. A separate worker fetches those jobs, performs a similarity search against a Qdrant vector store, and returns an OpenAI completion based on the retrieved context.

## Features

- FastAPI HTTP server for enqueuing RAG chat requests
- Redis-backed job queue via `rq`
- Qdrant vector search using `langchain-qdrant`
- OpenAI chat completion using `openai`

## Prerequisites

- Python 3.11+ (or compatible version)
- Redis server running on `localhost:6379`
- Qdrant server running on `http://localhost:6333`
- A Qdrant collection named `learning_rag`
- OpenAI API key available as an environment variable

## Installation

1. Create and activate your Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is in the repo root, run the command from the workspace root.

## Environment

Create a `.env` file in the `rag_queue` folder or the working directory used to run the app:

```ini
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://api.openai.com
```

## Running the API server

From the `rag_queue` directory:

```bash
cd rag_queue
python main.py
```

The API server listens on `http://0.0.0.0:8000`.

## Running the worker

The worker consumes jobs from Redis and executes `process_query`.

From the `rag_queue` directory:

```bash
PYTHONPATH=. rq worker default
```

## API Endpoints

### `GET /`

Health check endpoint.

Response:

```json
{ "status": "Server is up and running" }
```

### `POST /chat`

Enqueue a chat query.

Query parameter:

- `query` — the user question to answer

Example:

```bash
curl -X POST "http://localhost:8000/chat?query=What+is+RAG?"
```

Response:

```json
{ "status": "queued", "job_id": "<job_id>" }
```

### `GET /job-status`

Fetch the result of a queued job.

Query parameter:

- `job_id` — the ID returned by `/chat`

Example:

```bash
curl "http://localhost:8000/job-status?job_id=<job_id>"
```

Response:

```json
{ "result": "..." }
```

## Notes

- The worker assumes a Qdrant collection named `learning_rag` already exists and contains vectorized document chunks.
- The result endpoint calls `job.return_value()` to retrieve the completed output.
- If the worker has not finished yet, the job may not return a value immediately.

## Customization

- Update `queue/worker.py` to change the prompt, search behavior, or completion model.
- Update `server.py` to add extra metadata, request validation, or job routing.

## Troubleshooting

- If Redis is unavailable, the queue will fail to enqueue jobs.
- If Qdrant is unavailable or the collection is missing, similarity search will fail.
- Verify that `OPENAI_API_KEY` is set and valid for the OpenAI client.
