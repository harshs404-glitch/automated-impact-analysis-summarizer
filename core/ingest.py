import tempfile
from pdfminer.high_level import extract_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def extract_and_chunk(uploaded_files):
    """Takes Streamlit UploadedFile list -> returns (chunks, metadatas)."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    all_chunks, metadatas = [], []

    for f in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(f.read())
            tmp_path = tmp.name

        try:
            text = extract_text(tmp_path)
        except Exception as e:
            # skip corrupt/unreadable PDF rather than crash whole batch
            print(f"[ingest] failed to extract {f.name}: {e}")
            continue

        if not text.strip():
            print(f"[ingest] {f.name} produced empty text — likely scanned/image PDF, skipping (no OCR in scope)")
            continue

        chunks = splitter.split_text(text)
        all_chunks.extend(chunks)
        metadatas.extend([{"source": f.name}] * len(chunks))

    return all_chunks, metadatas