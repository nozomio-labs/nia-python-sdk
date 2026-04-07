from enum import Enum


class AnswerFeedbackRequestSignal(str, Enum):
    THUMBS_DOWN = "thumbs_down"
    THUMBS_UP = "thumbs_up"

    def __str__(self) -> str:
        return str(self.value)
