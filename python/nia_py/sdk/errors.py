from __future__ import annotations


class NiaSDKError(Exception):
    """Base SDK error for high-level wrapper APIs."""


class NiaAPIError(NiaSDKError):
    """Raised when the API returns an error status."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"API error {status_code}: {message}")


class NiaTimeoutError(NiaSDKError):
    """Raised when a long-running operation exceeds timeout."""
