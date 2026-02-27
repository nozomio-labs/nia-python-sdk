from enum import Enum


class TracerRequestModeType0(str, Enum):
    TRACER_DEEP = "tracer-deep"
    TRACER_FAST = "tracer-fast"

    def __str__(self) -> str:
        return str(self.value)
