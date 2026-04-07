from enum import Enum


class SourceInteractionRequestAction(str, Enum):
    COLLAPSED = "collapsed"
    COPIED = "copied"
    DWELLED = "dwelled"
    EXPANDED = "expanded"
    NAVIGATED = "navigated"

    def __str__(self) -> str:
        return str(self.value)
