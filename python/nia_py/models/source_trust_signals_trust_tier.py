from enum import Enum


class SourceTrustSignalsTrustTier(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
