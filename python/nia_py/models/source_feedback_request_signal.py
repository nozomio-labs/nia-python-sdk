from enum import Enum


class SourceFeedbackRequestSignal(str, Enum):
    HELPFUL = "helpful"
    IRRELEVANT = "irrelevant"
    PARTIALLY_RELEVANT = "partially_relevant"

    def __str__(self) -> str:
        return str(self.value)
