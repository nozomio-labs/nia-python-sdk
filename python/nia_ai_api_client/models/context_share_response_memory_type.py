from enum import Enum


class ContextShareResponseMemoryType(str, Enum):
    EPISODIC = "episodic"
    FACT = "fact"
    PROCEDURAL = "procedural"
    SCRATCHPAD = "scratchpad"

    def __str__(self) -> str:
        return str(self.value)
