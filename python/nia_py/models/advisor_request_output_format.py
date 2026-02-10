from enum import Enum


class AdvisorRequestOutputFormat(str, Enum):
    CHECKLIST = "checklist"
    DIFF = "diff"
    EXPLANATION = "explanation"
    STRUCTURED = "structured"

    def __str__(self) -> str:
        return str(self.value)
