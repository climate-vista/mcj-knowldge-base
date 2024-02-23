import streamlit as st
import time
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
assistant_id = "asst_zSYzwqWaqFYutfRd8YVzqLLj"  # TODO: put in env file


# Set openAi client , assistant ai and assistant ai thread
# @st.cache_resource
def load_openai_client_and_assistant():
    client = OpenAI(api_key=api_key)
    my_assistant = client.beta.assistants.retrieve(assistant_id)
    thread = client.beta.threads.create()
    return client, my_assistant, thread


client, my_assistant, assistant_thread = load_openai_client_and_assistant()


# check in loop  if assistant ai parse our request
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


# initiate assistant ai response
def generate_response(user_input=""):
    message = client.beta.threads.messages.create(
        thread_id=assistant_thread.id,
        role="user",
        content=user_input,
    )

    run = client.beta.threads.runs.create(
        thread_id=assistant_thread.id,
        assistant_id=assistant_id,
    )

    run = wait_on_run(run, assistant_thread)

    # Retrieve all the messages added after our last user message
    messages = client.beta.threads.messages.list(
        thread_id=assistant_thread.id, order="asc", after=message.id
    )

    return messages.data[0].content[0].text.value


def main():
    st.set_page_config(page_title="MCJ Chatbot", page_icon=":earth_americas:")
    st.header("MCJ Chatbot")
    message = st.text_input("Enter your question here:")
    if message:
        response = generate_response(message)
        st.info(response)


if __name__ == "__main__":
    main()
