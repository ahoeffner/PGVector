import io
import os
from dotenv import load_dotenv

from HGFTokenizer import HGFTokenizer # In memory stream for MD
from docling.chunking import HybridChunker # Intelligent chunking from Docling
from docling.document_converter import DocumentConverter # Convert to MD format
from docling.datamodel.base_models import DocumentStream # In memory stream for MD


load_dotenv()
Tokens = int(os.getenv("MAXTOKENS"))


class Docling :
	def __init__(self) :
		self.tokenizer = HGFTokenizer()
		self.converter = DocumentConverter()

		self.chunker = HybridChunker(
			max_tokens=Tokens,
			merge_peers=True,
			tokenizer=self.tokenizer
		)


	def chunk(self,source:str, url:bool = False) -> list[str] :
		"""
		Chunks the input text using Docling's HybridChunker.
		"""

		if (not url) :
			source = DocumentStream(name="text.md", stream=io.BytesIO(source.encode('utf-8')))

		doc = self.converter.convert(source)

		iter = self.chunker.chunk(doc.document)
		chunks = [c.text for c in iter]

		return(chunks)



if __name__ == "__main__" :
	str = "Dette er en test. "
	docling = Docling()
	docling.chunk(str,False)