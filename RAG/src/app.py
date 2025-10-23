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
	chunks:list[str] = []
	response = Response(chunks=[])

	print(data)

	if (not data.b64 and not data.url) :
		raise HTTPException(
				status_code=400,
				detail="Either b64 (Base64 encoded text) or url must be provided."
			)

	if (data.url) :
		chunks = Api.chunk(data.url,True)
	else :
		try:
			text = base64.b64decode(data.b64).decode('utf-8')
			chunks = Api.chunk(text,False)

		except Exception:
			raise HTTPException(
				status_code=400,
				detail="Could not decode the Base64 text. Please ensure 'b64' is valid Base64 encoded UTF-8 content."
			)


	for text in chunks :
		embed = Api.embed(text)
		text = base64.b64encode(text.encode('utf-8'))

		chunk = ChunkEmbedding(
			text=text,
			embedding=embed
		)
		response.chunks.append(chunk)

	return(response)
