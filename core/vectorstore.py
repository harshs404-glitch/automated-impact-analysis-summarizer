import uuid
from langchain_community.vectorstores import Chroma
from config import EMBEDDING_MODEL, RETRIEVER_K

def build_vectorstore(chunks, metadatas):
    """Fresh in-memory Chroma collection per session — avoids disk collisions
    across concurrent demo runs/users."""
    if not chunks:
        raise ValueError("No chunks to index — all uploaded PDFs failed extraction")

    collection_name = f"session_{uuid.uuid4().hex[:8]}"
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=EMBEDDING_MODEL,
        metadatas=metadatas,
        collection_name=collection_name,
    )
    return vectordb

def get_retriever(vectordb, k=RETRIEVER_K):
    return vectordb.as_retriever(search_type="similarity", search_kwargs={"k": k})