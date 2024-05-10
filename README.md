# Langchain/Langflow for LLM Chatbot RAG Applications

This repository explores Large Language Models (LLMs) using Langchain and Langflow frameworks for Retriever-Augmented Generation (RAG) applications. Langchain is a framework that integrates LLMs with data retrieval systems, enabling context-based insights for chatbot applications. Langflow, on the other hand, is a conversational AI framework that leverages Langchain to process and respond to natural language queries effectively.
Streamlit is used to create a user-friendly interface for the applications.

## 3 Mini projects:
1) **Langflow Website Chatbot**: A chatbot solution to answer queries from a designated website. It uses Langchain and Astra DB to extract website content and generate accurate responses.
2) **Langchain Restaurant Idea Creator**: Idea maker that use sequential chains to first generate ideas, and then generate ideas based on the first ideas.
3) **Langchain URL Chatbot**: A more flexible chatbot that can answer questions from any URL. It uses Langchain and Chroma DB to process and respond to user queries effectively.

### General processing pipeline:   
(IMAGE)


### 1. Langflow Website Chatbot

Use Langflows's quick and visual interface to create a chatbot that can answer queries from a designated website. The chatbot uses Langchain and Astra DB to extract website content and generate accurate responses. Processing pipeline from [Santiago's RAG tutorial](https://www.youtube.com/watch?v=RWo4GDTZIsE).

1. **Data Extraction**:
   - Website content is segmented into chunks of size 1000, with overlap of 200 characters.
   - Vectorization of each chunk is done by using OpenAI's embedding model.
   - The vectorized chunks are stored in Astra DB as vector documents.

2. **Query Processing**:
   - User inputs a question.
   - The question is transformed into an embedding and a similarity search is conducted in the vector database.
   - The most relevant text chunks are retrieved as context.

3. **Response Generation**:
   - The context retrieved from the database is fed into the GPT3.5-turbo model, which generates a response based on the context, ensuring that answers are comprehensive and contextually accurate rather than merely keyword-based.

Demo video:    
(URL)


### 2. Langchain Restaurant Idea Creator
A creative idea creator that use sequential chains to generate ideas based on its own ideas.   
   Implementation follows [Codebasics langchain crash course](https://www.youtube.com/watch?v=nAmC7SoVLd8).

1) Use LLM to generate a restaurant name based on the selected cuisine.   
2) Then, generate fitting menu items based on the restaurant name.
3) Build into Streamlit for an interactive web app.

Demo video:
(URL)


### 3. Langchain URL Chatbot
A more flexible chatbot that can answer questions from any URL. It uses Langchain and Chroma DB to process and respond to user queries effectively. Demonstrated to fetch relevant info from Tiktok's long privacy policy. Code follows [Alejandro's tutorial](https://www.youtube.com/watch?v=bupx08ZgSFg).

1) Extract text from chosen URL.
2) Vectorize the text and store it in Chroma DB.
3) Process user queries and generate responses based on the URL content.

Demo video:   
(URL)
