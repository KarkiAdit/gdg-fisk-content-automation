from dataclasses import dataclass
from typing import List
from .common import ProjectSummary, Testimonial

@dataclass
class HomePageResponse:
    """
    Represents the response for the home page, including a home video URL,
    project summaries, and testimonials.
    """
    homeVideoUrl: str
    projectSummaries: List[ProjectSummary]
    testimonials: List[Testimonial]

    def to_dict(self):
        """
        Converts the HomePageResponse object to a dictionary.
        """
        return {
            "homeVideoUrl": self.homeVideoUrl,
            "projectSummaries": [summary.to_dict() for summary in self.projectSummaries],
            "testimonials": [testimonial.to_dict() for testimonial in self.testimonials],
        }