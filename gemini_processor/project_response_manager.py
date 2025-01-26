from .gemini_processor import GeminiProcessor
from models import Project
from .templates.base_project_template import BASE_PROJECT_TEMPLATE
from .values.base_project_template_values import BASE_PROJECT_TEMPLATE_VALUES
import json

class ProjectResponseManager():
    """
    A class that manages responses related to a specific project by interacting with the Gemini AI model.

    This class extracts and processes project data based on a predefined template, which is then 
    transformed into structured project information through AI-generated content.
    """
    
    project: Project = None
    project_template = BASE_PROJECT_TEMPLATE
    project_template_values = BASE_PROJECT_TEMPLATE_VALUES

    def __init__(self, input_readme):
        """
        Initializes the ProjectResponseManager with project information by interacting with the Gemini AI.

        The initialization process includes extracting project details using a text-based AI model.
        
        Raises:
            ValueError: If the project information cannot be processed or extracted successfully.
        """
        self.ai_manager = GeminiProcessor()
        self.project_template_values["input_readme"] = input_readme
        self.project = self._extract_project_from_text()

    def _extract_project_from_text(self):
        """
        Extracts project information from the provided project template and template values by interacting with the Gemini AI model.

        Args:
            project_template (str): The base template used to generate a project-related prompt.
            project_template_values (dict): A dictionary of values used in the project template.

        Returns:
            dict: A dictionary containing structured project data extracted from the AI response.

        Raises:
            ValueError: If the project information cannot be converted from text to a valid JSON object.
        """
        # Render project prompt based on the provided template and template values
        project_prompt = self.project_template.render(self.project_template_values)        
        # Get AI-generated content from the project prompt
        response = self.ai_manager.generate_content_from_text(project_prompt)    
        # Clean up the response to remove the JSON wrapper
        cleaned_json_string = response.strip("```json\n").strip("```")
        try:
            # Convert the cleaned string into a dictionary
            data = json.loads(cleaned_json_string)
        except json.JSONDecodeError:
            raise ValueError("Failed to decode the project response into a valid JSON object.")
        return data

if __name__ == "__main__":
    # Example usage
    input_readme = BASE_PROJECT_TEMPLATE_VALUES["input_readme"]
    project_response_ai = ProjectResponseManager(input_readme)
    print(project_response_ai.project)
