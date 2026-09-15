import openai
import os

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

text = input("Enter your question: ")

response = client.responses.create(
    model="gpt-5.6",
    input=text
)

print(response.output_text)








