import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

class PDFProcessor:
    def __init__(self, vector_store_path="./vector_store"):
        self.vector_store_path = vector_store_path
        self.embeddings = OpenAIEmbeddings()
        
    def extract_text_from_pdf(self, pdf_file):
        """Extrai texto de um arquivo PDF."""
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    
    def extract_text_from_txt(self, txt_file):
        """Extrai texto de um arquivo TXT."""
        text = txt_file.getvalue().decode("utf-8")
        return text
    
    def process_text(self, text):
        """Processa o texto, divide em chunks e cria embeddings."""
        # Dividir o texto em chunks menores
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_text(text)
        
        # Criar embeddings e armazenar em FAISS
        vectorstore = FAISS.from_texts(chunks, self.embeddings)
        
        # Opcional: criar diretório para armazenar vetores
        if not os.path.exists(self.vector_store_path):
            os.makedirs(self.vector_store_path)
        
        return vectorstore