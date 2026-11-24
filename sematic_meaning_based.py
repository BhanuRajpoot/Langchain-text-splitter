from pathlib import Path

from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

# SemanticChunker needs an embeddings model, which reads OPENAI_API_KEY.
load_dotenv()
load_dotenv(Path(__file__).resolve().parents[1] / "Langchain-chains" / ".env")

text = "Hello, how are you? I am fine, thank you."

# Splits where the meaning changes. It does not take chunk_size or chunk_overlap.
semantic_chunker = SemanticChunker(OpenAIEmbeddings())

chunks = semantic_chunker.split_text(text)

print(chunks)
