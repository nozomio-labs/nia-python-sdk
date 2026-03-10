from enum import Enum


class SourceAnnotationCreateRequestKind(str, Enum):
    GOTCHA = "gotcha"
    NOTE = "note"
    TIP = "tip"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
