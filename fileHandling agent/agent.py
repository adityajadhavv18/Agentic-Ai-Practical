from dotenv import load_dotenv
from openai import OpenAI
import requests
from pydantic import BaseModel, Field
from typing import Optional
import json
import os

load_dotenv()

client = OpenAI()

def run_command(cmd: str):
    result = os.system(cmd)
    return result

available_tools = {
    "run_command": run_command
}

SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using structured chain-of-thought style execution.

You operate in the following ordered steps:
START → PLAN → TOOL → OBSERVE → PLAN → OUTPUT

You must ALWAYS think in PLAN steps before taking any action.
You may take multiple PLAN steps.
You may call a TOOL when required.
After every TOOL call you MUST wait for OBSERVE input before continuing.
Finally you must provide an OUTPUT.

Rules:
- Strictly follow the JSON output format.
- Only perform ONE step per response.
- Do NOT combine multiple steps in a single response.
- Do NOT skip planning.
- Do NOT hallucinate tool outputs.
- Be precise and deterministic.

Output JSON Format:
{ "step": "START" | "PLAN" | "TOOL" | "OUTPUT", "content": "string", "tool": "string", "input": "string" }

Available Tool:
- run_command(cmd: str): Executes a linux system command and returns the command output.

Example 1:
START: List files in current directory

PLAN:
{ "step": "PLAN", "content": "User wants to see files in current directory. I should use a linux command to list directory contents." }

PLAN:
{ "step": "PLAN", "content": "The appropriate command for this is ls." }

TOOL:
{ "step": "TOOL", "tool": "run_command", "input": "ls" }

OBSERVE:
{ "step": "OBSERVE", "tool": "run_command", "output": "file1.py file2.txt folderA" }

PLAN:
{ "step": "PLAN", "content": "I have received the directory listing from the tool." }

OUTPUT:
{ "step": "OUTPUT", "content": "The current directory contains file1.py, file2.txt and folderA." }


Example 2:
START: Create a folder named test_folder

PLAN:
{ "step": "PLAN", "content": "User wants to create a new folder in the system." }

PLAN:
{ "step": "PLAN", "content": "The correct linux command for creating a directory is mkdir." }

TOOL:
{ "step": "TOOL", "tool": "run_command", "input": "mkdir test_folder" }

OBSERVE:
{ "step": "OBSERVE", "tool": "run_command", "output": "0" }

PLAN:
{ "step": "PLAN", "content": "Directory creation command has been executed successfully." }

OUTPUT:
{ "step": "OUTPUT", "content": "The folder test_folder has been created successfully." }
"""

print("\n\n\n")

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input params for the tool")


message_history = [
    { "role": "system", "content": SYSTEM_PROMPT },
]


while True:
    user_query = input("👉🏻 ")
    message_history.append({ "role": "user", "content": user_query })

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o-mini",
            response_format=MyOutputFormat,
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("🔥", parsed_result.content)
            continue

        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🛠️: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"🛠️: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({ "role": "developer", "content": json.dumps(
                { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
            ) })
            continue



        if parsed_result.step == "PLAN":
            print("🧠", parsed_result.content)
            continue

        if parsed_result.step == "OUTPUT":
            print("🤖", parsed_result.content)
            break

print("\n\n\n")

