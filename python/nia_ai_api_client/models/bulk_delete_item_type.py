from enum import Enum


class BulkDeleteItemType(str, Enum):
    CONTEXT = "context"
    DOCUMENTATION = "documentation"
    LOCAL_FOLDER = "local_folder"
    REPOSITORY = "repository"
    RESEARCH_PAPER = "research_paper"

    def __str__(self) -> str:
        return str(self.value)
