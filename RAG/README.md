# Embedding Service

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
- POST /index -> A list of base64 encoded chunks and the corresponding embedding vector
