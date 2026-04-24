from langchain.tools import tool

from ..context import AppContext

def make_search_document_tool(context: AppContext):
    @tool(response_format="content_and_artifact")
    def search_document(query: str):
        """A PDF dokumentumban kereséshez"""
        retrieved_docs = context.vector_store.similarity_search(
            query,
            k=context.config.retrieval_k,
        )

        if not retrieved_docs:
            return "Nem találtam releváns részt a dokumentumban.", []

        serialized = "\n\n".join(
            (
                f"Oldal: {doc.metadata.get('page_label', doc.metadata.get('page', 'N/A'))}\n"
                f"Tartalom: {doc.page_content}"
            )
            for doc in retrieved_docs
        )
        return serialized, retrieved_docs

    return search_document