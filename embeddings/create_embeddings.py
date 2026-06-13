from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
# Load documents
faq_loader = TextLoader("data/faq.txt")
policy_loader = TextLoader("data/policies.txt")

faq_docs = faq_loader.load()
policy_docs = policy_loader.load()

documents = faq_docs + policy_docs

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Create embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
db = FAISS.from_documents(
    docs,
    embedding
)

# Save vector database
db.save_local("vector_db")

print("FAISS Vector Database Created Successfully!")