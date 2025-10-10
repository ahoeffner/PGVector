# Reverse Text REST service

This small example exposes the `reverse_text` function (in `src/test.py`) as a REST service using FastAPI.

How to run

1. Activate the virtualenv in the project root (if you're using the provided `bin/activate`):

```bash
source ./bin/activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Start the server with uvicorn:

```bash
uvicorn src.app:app --reload --host 127.0.0.1 --port 8000
```

Endpoints

- GET /health -> health check
- POST /reverse with JSON {"text": "..."} -> returns reversed text
- GET /reverse/{text} -> returns reversed text (from path)
