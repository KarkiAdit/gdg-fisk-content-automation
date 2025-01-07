from dataclasses import dataclass
from typing import List
from .common import Testimonial, Metric, VideoContent

@dataclass
class CulturePageResponse:
    """
    Represents the response for the culture page, including a culture video, testimonials, and metrics.
    """
    culturePageVideo: VideoContent
    testimonials: List[Testimonial]
    metrics: List[Metric]

    def to_dict(self):
        """
        Converts the CulturePageResponse object to a dictionary.
        """
        return {
            "culturePageVideo": self.culturePageVideo.to_dict(),
            "testimonials": [testimonial.to_dict() for testimonial in self.testimonials],
            "metrics": [metric.to_dict() for metric in self.metrics],
        }