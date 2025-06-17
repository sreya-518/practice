from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("../../nke-10k-2023.pdf")
documents = loader.load()

for doc in documents:
    print("File:", doc.metadata['source'])
    print("Content:", doc.page_content[:100], "\n")