from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AppConfig:
    csv_path: Path
    pdf_path: Path
    embedding_model: str = "text-embedding-3-small"
    agent_model: str = "gpt-5-nano"
    retrieval_k: int = 4
    chunk_size: int = 1000
    chunk_overlap: int = 200
    allowed_operations: tuple[str, ...] = (
    "row_count",
    "column_list",
    "head",
    "mean",
    "sum",
    "min",
    "max")