import os
import requests
from urllib.parse import urlparse, unquote

class Api:
	def loadAndChunk(url:str) -> list[str] :
		URL = url = urlparse(url)
		return [f"This is a placeholder for content from {url.geturl()}."]
