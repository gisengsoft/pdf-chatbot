# 📚 PDF Chatbot - Gilson Silva

Um assistente inteligente que responde perguntas com base no conteúdo de documentos PDF e TXT usando IA generativa, embeddings e busca vetorial.

![PDF Chatbot Screenshot](docs/screenshot.png)

## 🌟 Funcionalidades

- Upload e processamento de arquivos PDF e TXT
- Geração de embeddings para busca semântica
- Interface de chat intuitiva com Streamlit
- Respostas baseadas no conteúdo dos documentos carregados
- Armazenamento do histórico de conversas em JSON

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem principal
- **LangChain**: Framework para aplicações de IA generativa
- **OpenAI**: Modelo de linguagem e embeddings
- **FAISS**: Biblioteca para busca vetorial eficiente
- **PyMuPDF**: Extração de texto de PDFs
- **Streamlit**: Interface gráfica interativa

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- Chave de API da OpenAI

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/gisengsoft/pdf-chatbot.git
   cd pdf-chatbot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure sua chave da API OpenAI:
   - Renomeie `.env.example` para `.env`
   - Adicione sua chave API: `OPENAI_API_KEY=sua-chave-aqui`

4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

### Utilização

1. Acesse a aplicação no navegador (geralmente http://localhost:8501)
2. Faça upload de um arquivo PDF ou TXT pelo painel lateral
3. Aguarde o processamento do documento
4. Faça perguntas sobre o conteúdo do documento
5. Salve o histórico de conversas quando desejar

## 📝 Processo de Desenvolvimento

O desenvolvimento deste projeto seguiu estas etapas:

1. **Planejamento**: Definição dos requisitos e estrutura do projeto
2. **Implementação do Processador de PDF**: Desenvolvimento do módulo para extrair e processar texto
3. **Integração com IA**: Configuração dos embeddings e do sistema de perguntas e respostas
4. **Interface de Usuário**: Criação da interface interativa com Streamlit
5. **Testes e Refinamentos**: Validação das funcionalidades e melhorias incrementais

## 🔍 Aprendizados e Insights

- A qualidade das respostas depende diretamente da segmentação adequada do documento
- Embeddings locais são mais lentos, mas oferecem maior privacidade
- O contexto fornecido ao modelo de IA precisa ser cuidadosamente limitado para evitar respostas genéricas

## 🔮 Melhorias Futuras

- [ ] Suporte a múltiplos usuários com autenticação
- [ ] Interface mais refinada com personalização de temas
- [ ] Geração automática de resumos por documento
- [ ] Suporte a novos formatos (ePub, DOCX, HTML)
- [ ] Embeddings locais para uso totalmente offline
- [ ] Processamento de tabelas e imagens dos PDFs

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
