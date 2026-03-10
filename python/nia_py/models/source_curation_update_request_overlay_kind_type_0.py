from enum import Enum


class SourceCurationUpdateRequestOverlayKindType0(str, Enum):
    CUSTOM = "custom"
    NIA_VERIFIED = "nia_verified"

    def __str__(self) -> str:
        return str(self.value)
