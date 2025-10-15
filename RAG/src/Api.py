import os
import requests
from urllib.parse import urlparse, unquote

class Api:
	def load(url:str) -> str :
		URL = url = urlparse(url)
		return f"This is a placeholder for content from {url.geturl()}."


	def chunk(text:str) -> list[str] :
		return [f"This is a placeholder for chunked content from the text: {text}"]


	def loadAndChunk(url:str) -> list[str] :
		text = Api.load(url)
		chunks = Api.chunk(text)
		return(chunks)