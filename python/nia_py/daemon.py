from __future__ import annotations

from typing import Any
from uuid import uuid4

import httpx

from .client import AuthenticatedClient
from .errors import UnexpectedStatus
from .sdk.errors import NiaAPIError
from .sdk.retry import call_with_retries


def _compact_dict(payload: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in payload.items() if value is not None}


class DaemonClient:
    def __init__(
        self,
        client: AuthenticatedClient,
        *,
        max_retries: int = 2,
        initial_backoff_seconds: float = 0.5,
    ):
        self._client = client
        self._max_retries = max_retries
        self._initial_backoff_seconds = initial_backoff_seconds

    @classmethod
    def from_api_key(
        cls,
        *,
        api_key: str,
        base_url: str = "https://apigcp.trynia.ai/v2",
        timeout_seconds: float = 60.0,
        max_retries: int = 2,
        initial_backoff_seconds: float = 0.5,
    ) -> DaemonClient:
        client = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=httpx.Timeout(timeout_seconds),
            raise_on_unexpected_status=True,
        )
        return cls(
            client,
            max_retries=max_retries,
            initial_backoff_seconds=initial_backoff_seconds,
        )

    def _request(
        self,
        method: str,
        path: str,
        *,
        payload: dict[str, Any] | None = None,
        retry: bool = True,
    ) -> Any:
        def make_request() -> Any:
            response = self._client.get_httpx_client().request(
                method,
                path,
                json=payload,
            )
            if response.status_code >= 400:
                raise UnexpectedStatus(response.status_code, response.content)
            if not response.content:
                return None

            try:
                return response.json()
            except ValueError:
                return response.text

        def make_request_without_retries() -> Any:
            try:
                return make_request()
            except UnexpectedStatus as exc:
                raise NiaAPIError(
                    exc.status_code,
                    exc.content.decode(errors="ignore"),
                ) from exc

        if not retry:
            return make_request_without_retries()

        return call_with_retries(
            make_request,
            max_retries=self._max_retries,
            initial_backoff_seconds=self._initial_backoff_seconds,
        )

    def create_source(
        self,
        *,
        path: str,
        display_name: str | None = None,
        detected_type: str | None = None,
        sync_filters: dict[str, Any] | None = None,
    ) -> Any:
        return self._request(
            "POST",
            "/daemon/sources",
            payload=_compact_dict(
                {
                    "path": path,
                    "display_name": display_name,
                    "detected_type": detected_type,
                    "sync_filters": sync_filters,
                }
            ),
            retry=False,
        )

    def list_sources(self) -> Any:
        return self._request("GET", "/daemon/sources")

    def push_sync(
        self,
        *,
        local_folder_id: str,
        files: list[dict[str, Any]],
        cursor: dict[str, Any] | None = None,
        stats: dict[str, Any] | None = None,
        connector_type: str | None = None,
        is_final_batch: bool | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        request_idempotency_key = idempotency_key or str(uuid4())
        return self._request(
            "POST",
            "/daemon/sync",
            payload=_compact_dict(
                {
                    "local_folder_id": local_folder_id,
                    "files": files,
                    "cursor": cursor or {},
                    "stats": stats or {},
                    "connector_type": connector_type,
                    "is_final_batch": is_final_batch,
                    "idempotency_key": request_idempotency_key,
                }
            ),
        )

    def resync(self, local_folder_id: str) -> Any:
        return self._request("POST", f"/daemon/sources/{local_folder_id}/resync")

    def delete_source(self, local_folder_id: str) -> Any:
        return self._request("DELETE", f"/daemon/sources/{local_folder_id}")

    def heartbeat(self, source_ids: list[str]) -> Any:
        return self._request(
            "POST",
            "/daemon/heartbeat",
            payload={"source_ids": source_ids},
        )

    def report_error(
        self,
        local_folder_id: str,
        *,
        error: str,
        path: str | None = None,
    ) -> Any:
        return self._request(
            "POST",
            f"/daemon/sources/{local_folder_id}/error",
            payload=_compact_dict(
                {
                    "error": error,
                    "path": path,
                }
            ),
        )
