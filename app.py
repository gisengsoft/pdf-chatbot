import streamlit as st
from dotenv import load_dotenv
import os
from pdf_processor import PDFProcessor
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import json
from datetime import datetime

# Carregar variáveis de ambiente (OPENAI_API_KEY)
load_dotenv()

# Verificar se a API key está configurada
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ OPENAI_API_KEY não encontrada. Crie um arquivo .env com sua chave API.")
    st.stop()

# Configurações
@st.cache_resource
def get_processor():
    return PDFProcessor()

def setup_qa_chain(vectorstore):
    """Configura a cadeia de QA para responder perguntas."""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def save_chat_history(history):
    """Salva o histórico do chat em arquivo JSON."""
    filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    return filename

def main():
    st.set_page_config(page_title="Chatbot PDF", page_icon="📚")
    st.title("📚 Chatbot Baseado em PDFs - Gilson Silva")
    
    # Inicializar o processador de PDF
    processor = get_processor()
    
    # Inicializar o histórico de chat na sessão
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Sidebar para upload de arquivo
    with st.sidebar:
        st.header("Carregar Documento")
        uploaded_file = st.file_uploader("Escolha um arquivo PDF ou TXT", type=["pdf", "txt"])
        
        if uploaded_file is not None:
            with st.spinner('Processando o documento...'):
                # Extrair texto dependendo do tipo de arquivo
                if uploaded_file.type == "application/pdf":
                    text = processor.extract_text_from_pdf(uploaded_file)
                else:
                    text = processor.extract_text_from_txt(uploaded_file)
                
                # Processar documentos
                vectorstore = processor.process_text(text)
                qa_chain = setup_qa_chain(vectorstore)
                
                st.session_state.qa_chain = qa_chain
                st.session_state.document_name = uploaded_file.name
                st.success(f"✅ Documento '{uploaded_file.name}' processado!")
        
        # Botão para salvar histórico
        if st.button("Salvar Histórico de Chat") and st.session_state.chat_history:
            filename = save_chat_history(st.session_state.chat_history)
            st.success(f"Histórico salvo em {filename}")
    
    # Exibir mensagens do histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Interface de chat
    if prompt := st.chat_input("Faça sua pergunta sobre o documento..."):
        if 'qa_chain' not in st.session_state:
            st.error("Por favor, carregue um documento primeiro!")
            st.stop()
            
        # Adicionar pergunta ao histórico
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Processar a resposta
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                result = st.session_state.qa_chain({"query": prompt})
                response = result["result"]
                st.markdown(response)
        
        # Adicionar resposta ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Salvar no histórico completo
        st.session_state.chat_history.append({
            "query": prompt,
            "response": response,
            "document": st.session_state.get("document_name", "unknown"),
            "timestamp": datetime.now().isoformat()
        })

if __name__ == "__main__":
    main()