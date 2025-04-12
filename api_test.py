from openai import OpenAI

# init client and connect to localhost server
client = OpenAI(
    base_url="http://localhost:8001",  # change the default port if needed
    api_key="fake-api-key",
)

# call API
chat_completion = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Hello, how are you?"
    }],
    model="model_name"
)

print(chat_completion)

# print the top "choice"
print(chat_completion.choices[0].message.content)