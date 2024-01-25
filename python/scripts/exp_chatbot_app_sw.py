import os
from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
#I had some name collisions so tried to rename this import of Pinecone
from langchain.vectorstores import Pinecone as PineconeVector
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from logging import getLogger
log = getLogger("test")
log.error("Starting")


st.set_page_config(page_title="MCJ Chatbot", page_icon=":earth_americas:")

# 1. Set up vector database and perform similarity search
#pinecone.init() has been deprecated - threw exception

api_key=os.getenv("PINECONE_API_KEY")
pc = Pinecone(  api_key  )  # find at app.pinecone.io

# environment=os.getenv("PINECONE_ENV"),  # next to api key in console

log.error("pinecone() successful")
embeddings = OpenAIEmbeddings()
index_name = "mcj-chatbot"

if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, metric="cosine", dimension=1536)
docsearch = PineconeVector.from_existing_index(index_name, embeddings)

#log.error("PineconeVector created")

def retrieve_docs(query):
    docs = docsearch.similarity_search(query, k=3)
    page_content_array = [doc.page_content for doc in docs]
    return page_content_array


# 3. Set up LLMChain and prompts
llm = ChatOpenAI(model="gpt-3.5-turbo")

template = """
You are a world class industry research analyst specialized in climate technology.
I will provide you with a list of transcripts from podcast interviews with climate startup founders.
Help me find and summarize the most relevant transcripts for my research.

Here are the transcripts I found for you:
{transcripts}

Below is a question for you. Please answer it in a few sentences:
{question}
"""

prompt = PromptTemplate(input_variables=["transcripts", "question"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)


# 4. Retrieve augmented generation
def generate_response(query):
    transcripts = retrieve_docs(query)
    response = chain.run(transcripts=transcripts, question=query)
    return response


# 5. Build a simple app
def main():

    st.header("MCJ Chatbot")
    message = st.text_input("Enter your question here:")
    if message:
        try:
            response = generate_response(message)
            st.info(response)

        except:
            st.info("Error received from OpenAI")

        

if __name__ == "__main__":
    main()
