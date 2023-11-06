import pinecone
import os
import streamlit as st
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# 1. Read in the text documents and embed them
loader = DirectoryLoader("/Users/sherrywang/Downloads/mcj_sample", glob="*.txt")
docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
docs = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()


# 2. Set up vector database and perform similarity search
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment=os.getenv("PINECONE_ENV"),  # next to api key in console
)
index_name = "mcj-chatbot"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, metric="cosine", dimension=1536)
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)


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
    st.set_page_config(page_title="MCJ Chatbot", page_icon=":earth_americas:")
    st.header("MCJ Chatbot")
    message = st.text_input("Enter your question here:")
    if message:
        response = generate_response(message)
        st.info(response)


if __name__ == "__main__":
    main()
