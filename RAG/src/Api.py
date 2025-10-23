import Docling
from urllib.parse import urlparse


class Api:
	def load(url:str) -> str :
		url = urlparse(url)
		return f"This is a placeholder for content from {url.geturl()}."


	def chunk(text:str) -> list[str] :
		docling = Docling()
		return docling.chunk(text)


	def loadAndChunk(url:str) -> list[str] :
		text = Api.load(url)
		chunks = Api.chunk(text)
		return(chunks)