from enum import Enum


class GrepSourceV2SourcesSourceIdGrepPostTypeType0(str, Enum):
    CONNECTOR = "connector"
    DOCUMENTATION = "documentation"
    GOOGLE_DRIVE = "google_drive"
    HUGGINGFACE_DATASET = "huggingface_dataset"
    LOCAL_FOLDER = "local_folder"
    REPOSITORY = "repository"
    RESEARCH_PAPER = "research_paper"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
