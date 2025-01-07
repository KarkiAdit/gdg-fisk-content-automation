from dataclasses import dataclass
from typing import Optional, List

@dataclass
class TextContent:
    """
    Represents text content with optional image URL and required content.
    """
    content: str
    imgUrl: Optional[str] = None

    def to_dict(self):
        """
        Converts the TextContent object to a dictionary.
        """
        return {
            "content": self.content,
            "imgUrl": self.imgUrl,
        }

@dataclass
class VideoContent:
    """
    Represents video content with a title, image URL, and list of genres.
    """
    title: str
    imgUrl: str
    videoUrl: str
    genres: List[str]

    def to_dict(self):
        """
        Converts the VideoContent object to a dictionary.
        """
        return {
            "title": self.title,
            "imgUrl": self.imgUrl,
            "videoUrl": self.videoUrl,
            "genres": self.genres,
        }

@dataclass
class Section:
    """
    Represents a section containing a list of text contents.
    """
    textContents: List[TextContent]

    def to_dict(self):
        """
        Converts the Section object to a dictionary.
        """
        return {
            "textContents": [text_content.to_dict() for text_content in self.textContents]
        }

@dataclass
class Testimonial:
    """
    Represents a testimonial with optional author details and content.
    """
    id: str
    content: str
    classification: str
    teamDomain: str
    authorImgUrl: Optional[str] = None
    author: Optional[str] = None

    def to_dict(self):
        """
        Converts the Testimonial object to a dictionary.
        """
        return {
            "id": self.id,
            "content": self.content,
            "classification": self.classification,
            "teamDomain": self.teamDomain,
            "authorImgUrl": self.authorImgUrl,
            "author": self.author,
        }

@dataclass
class NumericalStat:
    """
    Represents a numerical statistic, with a value and an indicator if it's a percentage.
    """
    value: float
    isPercent: bool

    def to_dict(self):
        """
        Converts the NumericalStat object to a dictionary.
        """
        return {
            "value": self.value,
            "isPercent": self.isPercent,
        }

@dataclass
class Goal:
    """
    Represents a goal with a heading and an associated numerical statistic.
    """
    heading: str  # Corrected data type to str
    stat: NumericalStat

    def to_dict(self):
        """
        Converts the Goal object to a dictionary.
        """
        return {
            "heading": self.heading,
            "stat": self.stat.to_dict(),
        }

@dataclass
class Metric:
    """
    Represents a metric with a heading, a statistic, subheading, and a list of goals.
    """
    metricHeading: str
    stat: NumericalStat
    metricSubHeading: str
    goals: List[Goal]

    def to_dict(self):
        """
        Converts the Metric object to a dictionary.
        """
        return {
            "metricHeading": self.metricHeading,
            "stat": self.stat.to_dict(),
            "metricSubHeading": self.metricSubHeading,
            "goals": [goal.to_dict() for goal in self.goals],
        }

@dataclass
class ProjectSummary:
    """
    Represents a project summary with ID, hero image, title, and overview section.
    """
    id: str
    projectHeroImg: str
    projectTitle: str
    overview: Section

    def to_dict(self):
        """
        Converts the ProjectSummary object to a dictionary.
        """
        return {
            "id": self.id,
            "projectHeroImg": self.projectHeroImg,
            "projectTitle": self.projectTitle,
            "overview": self.overview.to_dict(),
        }