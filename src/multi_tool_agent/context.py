from dataclasses import dataclass
from typing import Any
import pandas as pd
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .config import AppConfig

@dataclass
class AppContext:
    config: AppConfig
    df: pd.DataFrame
    vector_store: Any

def build_vector_store(config: AppConfig):
    loader = PyPDFLoader(str(config.pdf_path))
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        add_start_index=True,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = text_splitter.split_documents(pages)

    embeddings = OpenAIEmbeddings(model=config.embedding_model)
    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(documents=chunks)
    return vector_store

def build_context(config: AppConfig) -> AppContext:
    df = pd.read_csv(config.csv_path)
    vector_store = build_vector_store(config)

    return AppContext(
        config=config,
        df=df,
        vector_store=vector_store,
    )