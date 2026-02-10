from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

import httpx

from ..errors import UnexpectedStatus
from .errors import NiaAPIError

T = TypeVar("T")


def call_with_retries(
    fn: Callable[[], T],
    *,
    max_retries: int,
    initial_backoff_seconds: float,
) -> T:
    last_exception: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except UnexpectedStatus as exc:
            last_exception = exc
            if exc.status_code < 500 or attempt >= max_retries:
                raise NiaAPIError(exc.status_code, exc.content.decode(errors="ignore")) from exc
        except (httpx.TransportError, httpx.TimeoutException) as exc:
            last_exception = exc
            if attempt >= max_retries:
                raise

        sleep_seconds = initial_backoff_seconds * (2**attempt)
        time.sleep(sleep_seconds)

    if last_exception:
        raise last_exception
    raise RuntimeError("Retry loop exited unexpectedly")
