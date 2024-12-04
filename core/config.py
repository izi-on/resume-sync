PROMPT = """
Format the output as a valid JSON object with appropriate keys and values.
{format_instructions}

The JSON must also respect the following template:
The first key is 'root', and its value is a list of objects
each containing a 'title' key and a 'content' key, optionally they can also have a "duration" key. The "content"
field can either be a list of strings that will represent bullet points,
or it can be a simple text string.

Parse the following text and extract relevant information into JSON format.
Text: {input_text}
"""

RESUME_KEY = "resume"
