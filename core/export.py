import streamlit as st

def to_markdown_download(report_text, filename="impact_report.md"):
    st.download_button(
        label="Export as Markdown",
        data=report_text,
        file_name=filename,
        mime="text/markdown",
    )