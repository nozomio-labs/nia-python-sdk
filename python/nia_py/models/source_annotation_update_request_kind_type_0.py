from enum import Enum


class SourceAnnotationUpdateRequestKindType0(str, Enum):
    GOTCHA = "gotcha"
    NOTE = "note"
    TIP = "tip"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
