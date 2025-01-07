from dataclasses import dataclass
from typing import Optional, List
from .common import Section, VideoContent

@dataclass
class Project:
    """
    Represents a project with details such as ID, hero image, title, overview,
    problem statement, features, demo video, and relevant links.
    """
    id: str
    projectHeroImg: str
    projectTitle: str
    readTimeInMins: int
    overview: Section
    problemStatement: str
    features: Section
    demo: VideoContent
    relevantLinks: List[str]
    author: Optional[str] = None

    def to_dict(self):
        """
        Converts the Project object to a dictionary.
        """
        return {
            "id": self.id,
            "projectHeroImg": self.projectHeroImg,
            "projectTitle": self.projectTitle,
            "readTimeInMins": self.readTimeInMins,
            "overview": self.overview.to_dict(), 
            "problemStatement": self.problemStatement,
            "features": self.features.to_dict(),
            "demo": self.demo.to_dict(),
            "relevantLinks": self.relevantLinks,
            "author": self.author,
        }

@dataclass
class ProjectsPageResponse:
    """
    Represents the response for the projects page, including a list of projects.
    """
    projects: List[Project]

    def to_dict(self):
        """
        Converts the ProjectsPageResponse object to a dictionary.
        """
        return {
            "projects": [project.to_dict() for project in self.projects]
        }