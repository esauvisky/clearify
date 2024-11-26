import re
from openai import OpenAI
from constants import SYSTEM, EXAMPLE_PROMPTS

client = OpenAI()

def send_request(sentence):
    messages = [{"role": "system", "content": SYSTEM}]
    for example in EXAMPLE_PROMPTS:
        messages.append({"role": example["role"], "content": example["content"]})
    messages.append({"role": "user", "content": f"<input>{sentence}</input>"})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=2000,
        n=1
    )

    # Extract the content from the response
    content = response.choices[0].message.content

    # Use regex to find all outputs within <output> tags
    outputs = re.findall(r'<output>(.*?)</output>', content, re.DOTALL)

    # Strip any leading/trailing whitespace from each output
    return [output.strip() for output in outputs]
