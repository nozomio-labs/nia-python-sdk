from __future__ import annotations

from .errors import NiaAPIError, NiaSDKError, NiaTimeoutError

__all__ = ["NiaSDK", "NiaSDKError", "NiaAPIError", "NiaTimeoutError"]


def __getattr__(name: str):
    if name == "NiaSDK":
        from .client import NiaSDK

        return NiaSDK
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
