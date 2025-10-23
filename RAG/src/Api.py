from Docling import Docling
from HGFEmbeddings import HGFEmbeddings

docling = Docling()
embeddings = HGFEmbeddings()


class Api:
	def chunk(source:str, url:bool) -> list[str] :
		return docling.chunk(source,url)


	def embed(text:str) -> list[float] :
		return embeddings.embed(text)
