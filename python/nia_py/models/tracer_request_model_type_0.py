from enum import Enum


class TracerRequestModelType0(str, Enum):
    CLAUDE_HAIKU_4_5_20251001 = "claude-haiku-4-5-20251001"
    CLAUDE_OPUS_4_6 = "claude-opus-4-6"
    CLAUDE_OPUS_4_6_1M = "claude-opus-4-6-1m"

    def __str__(self) -> str:
        return str(self.value)
