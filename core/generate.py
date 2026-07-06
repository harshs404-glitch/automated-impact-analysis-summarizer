from config import LLM
from prompts.impact_prompt import IMPACT_PROMPT

RETRIEVAL_QUERY = "change request impact stakeholders systems risk dependencies"

def generate_impact_report(retriever):
    docs = retriever.invoke(RETRIEVAL_QUERY)

    if not docs:
        return "No relevant content retrieved from uploaded documents."

    context = "\n\n".join(
        f"[{d.metadata.get('source', 'unknown')}]: {d.page_content}"
        for d in docs
    )

    prompt = IMPACT_PROMPT.format(context=context)

    try:
        response = LLM.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Report generation failed: {e}"