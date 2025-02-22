JSON_SCHEMA = """{
  "type": "object",
  "properties": {
    "variations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "version": {
            "type": "string"
          }
        },
        "required": [
          "version"
        ]
      }
    }
  },
  "required": [
    "variations"
  ]
}"""

SYSTEM_PROMPT = """You are tasked with analyzing and reconstructing a given text. Your goal is to create varied versions that maintain the core message and tone, exploring different structures and expressions. These instructions serve as guidelines, with varying levels of requirement for adherence:

1. Use the same language as the original text. *(Required for all versions)*
2. Each version should have distinct sentence structures or expressions, preserving the core intent. *(Required for all versions)*
3. Maintain the essential message and meaning of the original text. *(At least 4 out of 5 versions)*
4. Explore diverse syntax and expression for variety in output. *(Required for all versions)*
5. Ensure it genuinely sounds like it originates from the same author, maintaining their unique voice. *(At least 4 out of 5 versions)*
6. Preserve any unique formatting (e.g., all lowercase, all uppercase, punctuation, etc.) from the original text. *(At least 3 out of 5 versions)*
7. Translate words in a different language that are enclosed in square brackets ([]), ensuring translations reflect the context rather than being literal. *(Required for all versions)*
8. Ignore minor typos or spelling errors, retaining them unless they significantly affect clarity. *(At least 3 out of 5 versions)*
9. Use proper Markdown structures where applicable, such as wrapping code in code blocks or enumerating items into lists if it enhances readability and makes sense. *(At least 3 out of 5 versions)*

Note: If additional instructions are provided, apply them to 4 out of the 5 versions.

Remember:
- The objective is to generate varied yet coherent versions, with each appearing as though authored by the original individual.
- Variation should explore informal language or slang as used in the original where applicable.

Create 5 different versions of the text based on these flexible yet prioritized guidelines. Provide each variation inside its own <output> tags, without additional commentary or explanations."""

EXAMPLE_PROMPTS = [
    # First example
    {"role": "user",
     "content": "<input>Do you still have the findings of the reversion of the communication protocol? I work with RE and would love to play around with that 😏</input>"},
    {"role": "assistant",
     "content": """
<output>Do you still have the results from reversing the communication protocol? I work in `RE` and would love to experiment with them 😏</output>
<output>Hey, do you happen to hold onto the findings from the communication protocol reversal? As someone who works with `RE`, I'd love to play around with that 😏</output>
<output>Do you still possess the communication protocol reversal findings? I work with `RE` and am eager to mess around with them 😏</output>
<output>By any chance, do you still have the insights from the reversed communication protocol? I'm into `RE` and would love to tinker with it 😏</output>
<output>Do you have the findings from when the communication protocol was reversed? Being in `RE`, I'd really like to dive into that 😏</output>""".strip()},

    # Second example
    {"role": "user",
     "content": "<input>Can you share the recent sales reports? I'm preparing for tomorrow's meeting, and it would really help.</input>"},
    {"role": "assistant",
     "content": """
<output>Could you send me the latest **sales reports**? I'm getting ready for tomorrow's meeting, and they would be a big help.</output>
<output>Would you mind sharing the recent _sales reports_? I'm preparing for the meeting tomorrow, and that information would really assist me.</output>
<output>Hey, can you provide the most recent `sales reports`? They'd be super helpful as I prep for tomorrow's meeting.</output>
<output>Do you have the latest sales data? I'm gearing up for the meeting tomorrow, and it would be really useful.</output>
<output>Any chance you could send over the recent sales reports? I'm getting ready for tomorrow's meeting, and I'd appreciate it.</output>""".strip()},

    # Third example
    {"role": "user",
     "content": "<input>have you checked out the new UI? we need feedback on this asap. let me know when you get a chance</input>"},
    {"role": "assistant",
     "content": """
<output>have you taken a look at the new **UI**? we need feedback on this asap. let me know when you get a chance</output>
<output>have you checked out the updated `user interface`? we're in need of feedback asap. hit me up when you're able</output>
<output>did you review the new ui yet? we urgently need your feedback. please inform me when you can</output>
<output>have you explored the new **UI**? feedback is needed asap. let me know when you have a moment</output>
<output>hey, did you get a chance to check out the new UI? we could use your feedback asap. give me a shout when you're free</output>""".strip()},

    # Fourth example (multi-line input)
    {"role": "user",
     "content": "<input>hey! did you finish reviewing the documentation? we're hoping to finalize the project scope by the end of the week.\n\nif you can, try to send me your thoughts by thursday. thx!</input>"},
    {"role": "assistant",
     "content": """
<output>hey! did you complete the documentation review? we're aiming to finalize the project scope by week's end.\n\nif possible, please send me your feedback by **thursday**. thx!</output>
<output>hey! have you wrapped up looking over the documentation? we're hoping to lock down the project scope before the week is out.\n\nif you can, shoot me your thoughts by **thursday**. thanks!</output>
<output>hey! did you finish going through the docs? we want to finalize the project's scope by the end of this week.\n\nplease try to send me your input by **thursday** if you can. thx!</output>
<output>hey! have you completed your review of the documentation? we're planning to finalize the project scope by **friday**.\n\nif you could get me your thoughts by **thursday**, that'd be great. thank you!</output>
<output>hey! finished checking out the documentation yet? we're aiming to wrap up the project scope by week's end.\n\nif possible, send me your feedback by **thursday**. thx!</output>""".strip()},

    # Fifth example (varying structure drastically)
    {"role": "user",
     "content": "<input>Are the Q3 results out yet? I've been waiting on them for ages and still no word. This is holding up our analysis!</input>"},
    {"role": "assistant",
     "content": """
<output>Are the **Q3 results** available yet? I've been waiting forever and haven't heard anything. This is delaying our analysis!</output>
<output>Have the `Q3 results` been released yet? I've been waiting on them for ages with no updates. Our analysis is being held up!</output>
<output>Any news on the **Q3 results**? It's been ages, and I still haven't heard a thing. This is stalling our analysis!</output>
<output>Are the **third-quarter results** out yet? I've been waiting endlessly without any word. This is impeding our analysis!</output>
<output>Do you know if the **Q3 results** have come out? I've been awaiting them for ages and still nothing. This is hindering our analysis!</output>""".strip()}
]
