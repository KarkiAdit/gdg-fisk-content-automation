from utils.samples.sample_project_template_values import *

EXPECTED_RESPONSE_FORMAT = """{
    "id": "str",
    "projectHeroImg": "str",
    "projectTitle": "str",
    "readTimeInMins": "int",
    "overview": {
        "textContents": [
            {
                "content": "str",
                "imgUrl": "str"
            }
        ]
    },
    "problemStatement": "str",
    "features": {
        "textContents": [
            {
                "content": "str",
                "imgUrl": "str"
            }
        ]
    },
    "demo": {
        "title": "str",
        "imgUrl": "str",
        "videoUrl": "str",
        "genres": ["List[str]"]
    },
    "relevantLinks": ["List[str]"],
    "author": "Optional[str]"
}"""

BASE_PROJECT_TEMPLATE_VALUES = {
    "input_readme": input_readme, # Contains the processed README input content
    "expected_response_format": EXPECTED_RESPONSE_FORMAT, # Contains the expected project response definition
    "example_readme": example_readme, # Contains an example readme for reference
    "example_output": example_output, # Contains an example output for reference
}
