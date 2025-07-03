
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_memory():
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def get_vector_store_memory():
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.load_local("faiss_index", embeddings)
    return vectorstore
