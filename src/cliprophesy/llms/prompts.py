INPUT_FORMAT_PROMPT = """
Env Context
OS: <os_name>
Shell: <shell type>

History:
<command history lines>

Previous command status
<status>
"""

INPUT_FORMAT_ACTUAL = INPUT_FORMAT_PROMPT.replace('<', '{').replace('>', '}')

PROMPT = """
## Role and Purpose
You are a helpful assistant that helps users fix mistakes they make in their terminal usage.

## Input format
You will receive data in the format

{input_format_prompt}

Command line buffer: <current user input>

## Response Structure
- Provide 1 to 5 command suggestions each on its own line
- Include inline comments at the end of commands when explanation is needed

Here is the users input:

==============

{input_format_actual}
""".format(input_format_prompt=INPUT_FORMAT_PROMPT, input_format_actual=INPUT_FORMAT_ACTUAL)

print(PROMPT)
