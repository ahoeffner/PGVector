from Docling import Docling
from HGFEmbeddings import HGFEmbeddings



class Api:
	def chunk(source:str, url:bool) -> tuple[str,list[str]] :
		docling = Docling()
		return docling.chunk(source,url)

	def embed(text:str) -> list[float] :
		embeddings = HGFEmbeddings()
		return embeddings.embed(text)
