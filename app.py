import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# 1. Load your document
loader = PyPDFLoader("data/example.pdf")
pages = loader.load()

# 2. Split text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(pages)

# 3. Embed with sentence-transformers
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Vector store
db = FAISS.from_documents(docs, embeddings)

# 5. Local LLM via Ollama
ollama_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
llm = Ollama(model="deepseek-r1:8b", base_url="http://localhost:11434")  # or llama3, phi3, etc.

# 6. RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

# 7. Simple CLI
print("📄 Local File Q&A Bot (type 'exit' to quit)")
while True:
    query = input("\nAsk a question: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = qa_chain(query)
    print("\nAnswer:", result["result"])
