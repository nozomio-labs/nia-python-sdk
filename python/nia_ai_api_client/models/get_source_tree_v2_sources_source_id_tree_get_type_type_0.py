from enum import Enum


class GetSourceTreeV2SourcesSourceIdTreeGetTypeType0(str, Enum):
    DOCUMENTATION = "documentation"
    HUGGINGFACE_DATASET = "huggingface_dataset"
    LOCAL_FOLDER = "local_folder"
    REPOSITORY = "repository"
    RESEARCH_PAPER = "research_paper"

    def __str__(self) -> str:
        return str(self.value)
