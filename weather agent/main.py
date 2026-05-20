from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def main():
    user_query = input("Enter your query: ")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [
            {"role":"user", "content": user_query}
        ]
    )

    print("Response:", response.choices[0].message.content)
main()