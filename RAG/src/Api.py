from Docling import Docling


class Api:
	def chunk(source:str, url:bool) -> list[str] :
		docling = Docling()
		return docling.chunk(source,url)
