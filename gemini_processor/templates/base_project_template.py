from jinja2 import Template

BASE_PROJECT_TEMPLATE = Template(
"""
The following readme is a project's design documentation. Analyze it and extract important project information in the expected json format:

**Project Description:**
{{ input_readme }}

**Expected Format:**
{{ expected_response_format }}

**Instructions:**
1. Based on the project description, determine appropriate values for each field in JSON format.
2. Associate images where needed and be creative figuring out each section.
2. Provide the extracted information in the JSON format as shown in the example.
4. Don't drop any JSON field and make every part unique but technical.

**Example Project Description:**
{{ example_readme }}

**Expected JSON Format:**
{{ example_output }} 

**Guidelines:**
* Extract only the most relevant information.
* Ensure the output is in the correct JSON format.
* Be concise but don't remove any technical details.
"""
)