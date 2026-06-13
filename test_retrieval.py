from modules.retrieval import search_documents

results = search_documents("refund policy")

for doc in results:
    print(doc.page_content)
    print("-" * 50)