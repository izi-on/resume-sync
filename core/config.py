PROMPT = """
Format the output as a valid JSON object with appropriate keys and values.
{format_instructions}

The JSON must also respect the following template:
The first key is 'root', and its value is a list of objects
each containing a 'title' key and a 'content' key. The 'content'
field has to be a list, it can be a list of strings that will represent bullet points, 
or it can also be a list of 'title' and 'content' objects as described above. 
NO OTHER KEYS ARE ALLOWED.

Ensure that all URLs specify the https:// protocol as the prefix

Make sure that the objects that are direct children of the "root"
contain ONLY the following titles. If the titles differ but share 
the same meaning, rewrite them:

{allowed_titles}

If the object is not a direct child of the root, it can have
any title.

Parse the following text and extract relevant information into JSON format.
Text: {input_text}
"""

RESUME_KEY = "resume"

ALLOWED_TITLES = [
    "Contact Information",
    "Education",
    "Professional Experience",
    "Projects",
    "Awards",
    "Skills",
]
