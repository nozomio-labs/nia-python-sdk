from enum import Enum


class DeleteSourceV2SourcesSourceIdDeleteTypeType0(str, Enum):
    DOCUMENTATION = "documentation"
    HUGGINGFACE_DATASET = "huggingface_dataset"
    LOCAL_FOLDER = "local_folder"
    REPOSITORY = "repository"
    RESEARCH_PAPER = "research_paper"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
