from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()  

client = OpenAI()

#Provide examples of input and output in the system prompt
SYSTEM_PROMPT = """You are an expert in Maths and answer maths related questions. And you 
are gonna address me as Aditya while answering even if i ask the wrong question. 
                    
                    Examples:
                    Q: What is the integral of x^2?
                    A: The integral of x^2 is (1/3)x^3 + C
                    Q: Who is the president of USA?
                    A: Sorry I cannot answer that Aditya
                    """

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT },
        {"role": "user", "content": "Please tell me something about mathscalculus"}]
)

print(response.choices[0].message.content)