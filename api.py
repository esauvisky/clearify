import re
from loguru import logger
from openai import OpenAI
from constants import SYSTEM, EXAMPLE_PROMPTS

client = OpenAI()

def send_request(sentence, previous_outputs=None, extra_instructions=None):
    messages = [{"role": "system", "content": SYSTEM}]
    for example in EXAMPLE_PROMPTS:
        messages.append({"role": example["role"], "content": example["content"]})
    logger.info(f"Sent {len(messages)} messages to the API.")
    # Include the initial input
    messages.append({"role": "user", "content": f"<input>{sentence}</input>"})

    if previous_outputs and extra_instructions:
        # Include previous outputs and extra instructions
        outputs_text = '\n'.join([f"<output>{output}</output>" for output in previous_outputs])
        messages.append({"role": "assistant", "content": outputs_text})
        messages.append({"role": "user", "content": f"Please refine 4 of the 5 versions according to the following instructions: '{extra_instructions}'"})

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
