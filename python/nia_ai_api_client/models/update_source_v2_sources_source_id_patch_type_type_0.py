from enum import Enum


class UpdateSourceV2SourcesSourceIdPatchTypeType0(str, Enum):
    DOCUMENTATION = "documentation"
    HUGGINGFACE_DATASET = "huggingface_dataset"
    LOCAL_FOLDER = "local_folder"
    REPOSITORY = "repository"
    RESEARCH_PAPER = "research_paper"

    def __str__(self) -> str:
        return str(self.value)
