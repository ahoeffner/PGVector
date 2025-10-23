import os
import torch
from dotenv import load_dotenv
from transformers import AutoModel, AutoTokenizer

load_dotenv()


class HGFEmbeddings:
	"""
	Class for generating embeddings using the Hugging Face Transformers library.
	"""

	def __init__(self) :
		model = os.getenv("HGFMODEL")

		self.model = AutoModel.from_pretrained(model)
		self.tokenizer = AutoTokenizer.from_pretrained(model)


	def embed(self, text:str) -> list[float] :
		tokens = self.tokenizer(
			[text],
			padding=True,
			truncation=True,
			return_tensors='pt')

		with torch.no_grad() :
			outputs = self.model(**tokens)

		attention = tokens['attention_mask']
		embeddings = outputs.last_hidden_state

		expanded = attention.unsqueeze(-1).expand(embeddings.size()).float()

		embeddings = torch.sum(embeddings * expanded, 1)
		sum_mask = torch.clamp(expanded.sum(1), min=1e-9) # Avoid division by zero
		embedding = embeddings / sum_mask

		return(embedding.squeeze(0).tolist())
