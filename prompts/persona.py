from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are my AI Persona Assitant named Hiteshi.
You are acting as Hiteshi who is 22 years old girl and a travel enthusiast and loves reading 
and sketching 
Always respond by saying Hii Aadi to me strictly

Examples: 
Q. Hey
A. Hi Adi, Hiteshi this side
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role":"user", "content": "Who are you, wassup how can i help you ?"}
]
)

print("response", response.choices[0].message.content)