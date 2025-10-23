import os
from dotenv import load_dotenv
from transformers import AutoTokenizer
from transformers.tokenization_utils_base import PreTrainedTokenizerBase

load_dotenv()


class HGFTokenizer(PreTrainedTokenizerBase) :
	"""
	A custom tokenizer that inherits from PreTrainedTokenizerBase.
	This class can be extended to implement specific tokenization logic.
	"""

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		model = os.getenv("HGFMODEL")
		self.tokenizer = AutoTokenizer.from_pretrained(model)

		self.vocab = self.tokenizer.vocab
		# self.unk_token = self.tokenizer.unk_token
		# self.pad_token = self.tokenizer.pad_token
		# self.cls_token = self.tokenizer.cls_token
		# self.sep_token = self.tokenizer.sep_token
		# self.bos_token = self.tokenizer.bos_token
		# self.eos_token = self.tokenizer.eos_token
		# self.mask_token = self.tokenizer.mask_token
		# self.ids_to_tokens = self.tokenizer.ids_to_tokens
		self.model_max_length = self.tokenizer.model_max_length

	def tokenize(self, text: str, **kwargs) -> list[str]:
		"""
		Tokenizes the input text using the underlying tokenizer.
		This method is explicitly called by Docling's internal tokenizer wrapper.
		"""
		return self.tokenizer.tokenize(text, **kwargs)


	def _tokenize(self, text:str, **kwargs) -> list[str] :
		"""
		Tokenizes the input text using the underlying tokenizer.
		"""
		return self.tokenizer.tokenize(text,kwargs)


	def _convert_token_to_id(self, token: str) -> int:
		"""
		Converts a single token string to its numerical ID.
		"""
		return self.tokenizer._convert_token_to_id(token)


	def _convert_id_to_token(self, index: int) -> str:
		"""
		Converts a single numerical ID to its token string.
		"""
		return self.tokenizer._convert_id_to_token(index)


	def get_vocab(self) -> dict:
		"""
		Returns the tokenizer's vocabulary as a dictionary mapping tokens to IDs.
		"""
		return self.tokenizer.get_vocab()


	def __len__(self) -> int:
		"""
		Returns the size of the vocabulary.
		This is typically the number of unique tokens in the tokenizer's vocabulary.
		"""
		return len(self.tokenizer)


	def encode(self, text: str, **kwargs) -> list[int]:
		"""
		Encodes text to a list of token IDs.
		"""
		# The base class's encode method usually calls _tokenize and _convert_token_to_id.
		# You can either rely on super().encode() or delegate directly.
		return self.tokenizer.encode(text, **kwargs)


	def decode(self, token_ids: list[int], **kwargs) -> str:
		"""
		Decodes a list of token IDs back to a string.
		"""
		# The base class's decode method usually calls _convert_id_to_token.
		return self.tokenizer.decode(token_ids, **kwargs)