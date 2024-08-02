from openai import OpenAI

api_client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
chat_log = [
    {"role": "system",
     "content": "You are a research assistant. Your task is to provide accurate and thorough information on various topics, ensuring that all responses are well-supported and informative."},
    {"role": "user",
     "content": "Hello, introduce yourself to someone using this program for the first time. Be concise and professional."},
]

while True:
    response = api_client.chat.completions.create(
        model="local-model",
        messages=chat_log,
        temperature=0.7,
        stream=True,
    )

    assistant_message = {"role": "assistant", "content": ""}

    for part in response:#reading chunks from the response returned from the model
        if part.choices[0].delta.content:
            print(part.choices[0].delta.content, end="", flush=True)
            assistant_message["content"] += part.choices[0].delta.content

    chat_log.append(assistant_message)

    print()
    chat_log.append({"role": "user", "content": input("> ")})