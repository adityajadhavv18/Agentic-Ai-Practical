from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()  

client = OpenAI()

SYSTEM_PROMPT = """You are an expert in Maths and only and only answer maths related questions. 
                    If the query is not related to maths just say sorry i cannot answer"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT },
        {"role": "user", "content": "Please tell me something about integration"}]
)

print(response.choices[0].message.content)