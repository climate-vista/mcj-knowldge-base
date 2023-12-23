from openai import OpenAI


client = OpenAI()

mcj_bot_id = "asst_aGeYTHGLPepC6tps1gAhuHrY"
# mcj_bot = client.beta.assistants.retrieve(mcj_bot_id)
mcj_bot = client.beta.assistants.update(
    mcj_bot_id,
    tools=[],
)
mcj_bot = client.beta.assistants.retrieve(mcj_bot_id)
print(mcj_bot)

# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "List the climate technologies based on the transcripts",
#         }
#     ]
# )
# print(thread.id)
# run = client.beta.threads.runs.create(
#   thread_id=thread.id,
#   assistant_id=mcj_bot.id
# )

messages = client.beta.threads.messages.list("thread_Ohtv8KuHOMoKL9NQrCcMXkQ0")
# message = client.beta.threads.messages.retrieve(
#     thread_id=thread.id,
#     message_id="msg_Y7wsGLej9rDcSKctJ9Xo1uJ0",
# )

# Extract the message content
message_content = messages.data[0].content[0].text
annotations = message_content.annotations
citations = []

# Iterate over the annotations and add footnotes
for index, annotation in enumerate(annotations):
    # Replace the text with a footnote
    message_content.value = message_content.value.replace(
        annotation.text, f" [{index}]"
    )

    # Gather citations based on annotation attributes
    if file_citation := getattr(annotation, "file_citation", None):
        cited_file = client.files.retrieve(file_citation.file_id)
        citations.append(f"[{index}] {file_citation.quote} from {cited_file.filename}")
    elif file_path := getattr(annotation, "file_path", None):
        cited_file = client.files.retrieve(file_path.file_id)
        citations.append(f"[{index}] Click <here> to download {cited_file.filename}")
        # Note: File download functionality not implemented above for brevity

# Add footnotes to the end of the message before displaying to user
message_content.value += "\n" + "\n".join(citations)
print(message_content.value)
