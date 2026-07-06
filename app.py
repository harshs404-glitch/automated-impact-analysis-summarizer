import streamlit as st
from config import LLM, EMBEDDING_MODEL
from core.ingest import extract_and_chunk
from core.vectorstore import build_vectorstore, get_retriever
from core.generate import generate_impact_report
from core.export import to_markdown_download

st.set_page_config(page_title="Impact Analysis Summarizer")
st.title("Brevity")

files = st.file_uploader("Upload docs (CR / feedback / specs)", type="pdf", accept_multiple_files=True)

if files and st.button("Generate Impact Report"):
    with st.spinner("Extracting & chunking..."):
        chunks, metadatas = extract_and_chunk(files)

    with st.spinner("Indexing documents..."):
        vectordb = build_vectorstore(chunks, metadatas)
        retriever = get_retriever(vectordb)

    with st.spinner("Generating structured report..."):
        report = generate_impact_report(retriever)

    st.subheader("Impact Analysis Report")
    st.markdown(report)
    to_markdown_download(report)
    