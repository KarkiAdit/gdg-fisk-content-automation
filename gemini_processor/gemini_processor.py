from config.auth import get_gemini_model
from vertexai.generative_models import Part

class GeminiProcessor:
    """
    Interacts with the Gemini AI system to generate responses based on text, images, or both.
    
    This class provides methods to generate content using Google's Gemini Generative AI model.
    It supports three types of content generation:
    
    1. Text-based content generation from a text prompt.
    2. Image-based content generation from an image and a question.
    3. Combined text and image-based content generation.
    
    Attributes:
        gemini_model (GenerativeModel): The authenticated Gemini model used for content generation.
    """

    def __init__(self):
        """
        Initializes the Gemini client with authentication.
        """
        self.gemini_model = get_gemini_model()  # Authenticated Gemini model

    def generate_content_from_text(self, text):
        """
        Generates content based on a provided text prompt.

        Args:
            text (str): The text prompt for content generation.

        Returns:
            str: The generated content (response text).
        """
        response = self.gemini_model.generate_content([text])
        return response.text

    def generate_content_from_image(self, image_uri, question):
        """
        Generates content based on an image and a related text prompt.

        Args:
            image_uri (str): The URI of the image stored in Google Cloud Storage (GCS).
            question (str): The question related to the image.

        Returns:
            str: The generated content (response text).
        """
        response = self.gemini_model.generate_content(
            [
                Part.from_uri(image_uri, mime_type="image/png"),
                question,
            ]
        )
        return response.text

    def generate_content_from_text_and_image(self, image_uri, question, text):
        """
        Generates content based on both an image and a text prompt.

        Args:
            image_uri (str): The URI of the image stored in Google Cloud Storage (GCS).
            question (str): The question related to the image.
            text (str): The text prompt for content generation.

        Returns:
            str: The generated content (response text).
        """
        response = self.gemini_model.generate_content(
            [
                Part.from_uri(image_uri, mime_type="image/png"),
                question,
                text,
            ]
        )
        return response.text

# # Example Usage
# if __name__ == "__main__":
#     # Initialize the GeminiProcessor class
#     processor = GeminiProcessor()
#     # Example usage for generating content from text
#     text = "What is the capital of France?"
#     print("Generating content from text:")
#     generated_text = processor.generate_content_from_text(text)
#     print(generated_text)
#     # Example usage for generating content from an image and a question
#     image_uri = "gs://gdg-fisk-assets/images/304a19161f0041ffb47027d4a1f1e2fc.png"
#     question = "What is in this image?"
#     print("\nGenerating content from image and question:")
#     generated_image_content = processor.generate_content_from_image(image_uri, question)
#     print(generated_image_content)
#     # Example usage for generating content from both text and image
#     text = "Describe what you see in the image."
#     print("\nGenerating content from both text and image:")
#     generated_combined_content = processor.generate_content_from_text_and_image(image_uri, question, text)
#     print(generated_combined_content)
