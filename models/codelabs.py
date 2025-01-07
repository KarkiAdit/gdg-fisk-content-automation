from dataclasses import dataclass
from typing import Optional, List

@dataclass
class KeyLearning:
    """
    Represents a key learning item with content and an optional icon.
    """
    content: str
    icon: Optional[str] = None

    def to_dict(self):
        """
        Converts the KeyLearning object to a dictionary.
        """
        return {
            "content": self.content,
            "icon": self.icon,
        }

@dataclass
class Codelab:
    """
    Represents a codelab with its details, including key learnings.
    """
    id: str
    screenshotUrl: str
    gcsUrl: str
    title: str
    keyLearnings: List[KeyLearning]
    releasedDate: str
    author: Optional[str] = None

    def to_dict(self):
        """
        Converts the Codelab object to a dictionary.
        """
        return {
            "id": self.id,
            "screenshotUrl": self.screenshotUrl,
            "gcsUrl": self.gcsUrl,
            "title": self.title,
            "keyLearnings": [learning.to_dict() for learning in self.keyLearnings],
            "releasedDate": self.releasedDate,
            "author": self.author,
        }

@dataclass
class CodelabsPageResponse:
    """
    Represents the response for the codelabs page, including a list of codelabs.
    """
    codelabs: List[Codelab]

    def to_dict(self):
        """
        Converts the CodelabsPageResponse object to a dictionary.
        """
        return {
            "codelabs": [codelab.to_dict() for codelab in self.codelabs]
        }