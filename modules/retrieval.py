from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_db",
    embedding,
    allow_dangerous_deserialization=True
)

def search_documents(query):

    docs = db.similarity_search(
        query,
        k=2
    )

    return docs