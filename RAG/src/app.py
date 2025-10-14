import base64
from src.Api import Api
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


# Define the input schema for this service
class Request(BaseModel):
    url: Optional[str] = None
    b64: Optional[str] = None


# Define the response schema of this service
class ChunkEmbedding(BaseModel):
    """Structure for a single text chunk and its simulated embedding."""
    text: str
    embedding: list[float]

class Response(BaseModel):
    """The final response containing all text chunks and embeddings."""
    chunks: list[ChunkEmbedding]



app = FastAPI(title="Embedding Service")


@app.get("/health")
def health():
   return {"status": "ok"}


@app.post("/index")
async def index(data: Request) -> Response :
	# Updated validation check
	if (not data.b64 and not data.url) :
		raise HTTPException(
				status_code=400,
				detail="Either b64 (Base64 encoded text) or url must be provided."
			)

	chunks:list[str] = []

	if (data.url) :
		# Placeholder for URL processing logic
		chunks = Api.loadAndChunk(data.url)
	else :
		# Decode the base64 text
		try:
			chunks[0] = base64.b64decode(data.b64).decode('utf-8')
		except Exception:
			raise HTTPException(
				status_code=400,
				detail="Could not decode the Base64 text. Please ensure 'b64' is valid Base64 encoded UTF-8 content."
			)

	return Response(chunks=[])
