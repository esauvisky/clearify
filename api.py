import json
import re
from loguru import logger
from openai import OpenAI
from constants import EXAMPLE_GEMINI_PROMPTS, JSON_SCHEMA, SYSTEM_PROMPT, EXAMPLE_PROMPTS
import google.generativeai as genai
# from google.generativeai import protos
from google.generativeai.types import HarmCategory, HarmBlockThreshold
# from google.ai.generativelanguage_v1beta.types import content

client = OpenAI()


def send_request(sentence, previous_outputs=None, extra_instructions=None):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for example in EXAMPLE_PROMPTS:
        messages.append({"role": example["role"], "content": example["content"]})
    logger.info(f"Sent {len(messages)} messages to the API.")
    # Include the initial input
    messages.append({"role": "user", "content": f"<input>{sentence}</input>"})

    if previous_outputs and extra_instructions:
        # Include previous outputs and extra instructions
        outputs_text = '\n'.join([f"<output>{output}</output>" for output in previous_outputs])
        messages.append({"role": "assistant", "content": outputs_text})
        messages.append({
            "role": "user", "content": f"Please refine 4 of the 5 versions according to the following instructions: '{extra_instructions}'"})

    response = client.chat.completions.create(model="gpt-4o-mini",
                                              messages=messages,
                                              temperature=1,
                                              frequency_penalty=0,
                                              presence_penalty=0,
                                              max_tokens=2000,
                                              n=1)

    # Extract the content from the response
    content = response.choices[0].message.content

    # Use regex to find all outputs within <output> tags
    outputs = re.findall(r'<output>(.*?)</output>', content, re.DOTALL)

    # None
    return [output.strip() for output in outputs]


chat_session = None


def send_request_with_gemini(prompt_data):
    # Create the model
    generation_config = {
        "temperature": 0.5,
        "max_output_tokens": 8192,}

    model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp",
                                  generation_config=generation_config,
                                  safety_settings={
                                      HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                      HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                                      HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                                      HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,},
                                  system_instruction=SYSTEM_PROMPT)

    chat_session = model.start_chat(history=EXAMPLE_GEMINI_PROMPTS)

    response = chat_session.send_message(f"<input>{prompt_data}</input>")
    content = response.text

    # Use regex to find all outputs within <output> tags
    outputs = re.findall(r'<output>(.*?)</output>', content, re.DOTALL)

    # None
    print(response)
    return [output.strip() for output in outputs]
