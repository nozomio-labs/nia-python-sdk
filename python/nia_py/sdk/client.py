from __future__ import annotations

import json
import time
from collections.abc import Generator
from dataclasses import dataclass
from typing import Any

import httpx

from ..api.default import (
    create_oracle_job_v2_oracle_jobs_post,
    get_oracle_job_v2_oracle_jobs_job_id_get,
    list_oracle_jobs_v2_oracle_jobs_get,
)
from ..api.v2_api import (
    create_source_v2_sources_post,
    delete_source_v2_sources_source_id_delete,
    get_source_v2_sources_source_id_get,
    list_sources_v2_sources_get,
    resolve_source_v2_sources_resolve_get,
    unified_search_v2_v2_search_post,
)
from ..client import AuthenticatedClient
from ..models.deep_research_request_with_mode import DeepResearchRequestWithMode
from ..models.oracle_research_request import OracleResearchRequest
from ..models.query_search_request import QuerySearchRequest
from ..models.query_search_request_messages_item import QuerySearchRequestMessagesItem
from ..models.source_create_request import SourceCreateRequest
from ..models.universal_search_request_with_mode import UniversalSearchRequestWithMode
from ..models.web_search_request_with_mode import WebSearchRequestWithMode
from .errors import NiaTimeoutError
from .retry import call_with_retries

TERMINAL_JOB_STATUSES = {"completed", "failed", "cancelled"}


@dataclass
class RetryConfig:
    max_retries: int = 2
    initial_backoff_seconds: float = 0.5


class SearchClient:
    def __init__(self, client: AuthenticatedClient, retry_config: RetryConfig):
        self._client = client
        self._retry_config = retry_config

    def query(self, *, messages: list[dict[str, Any]], **kwargs: Any) -> Any:
        body = QuerySearchRequest(
            messages=[QuerySearchRequestMessagesItem.from_dict(message) for message in messages],
            **kwargs,
        )
        return call_with_retries(
            lambda: unified_search_v2_v2_search_post.sync(client=self._client, body=body),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def web(self, *, query: str, **kwargs: Any) -> Any:
        body = WebSearchRequestWithMode(query=query, **kwargs)
        return call_with_retries(
            lambda: unified_search_v2_v2_search_post.sync(client=self._client, body=body),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def deep(self, *, query: str, **kwargs: Any) -> Any:
        body = DeepResearchRequestWithMode(query=query, **kwargs)
        return call_with_retries(
            lambda: unified_search_v2_v2_search_post.sync(client=self._client, body=body),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def universal(self, *, query: str, **kwargs: Any) -> Any:
        body = UniversalSearchRequestWithMode(query=query, **kwargs)
        return call_with_retries(
            lambda: unified_search_v2_v2_search_post.sync(client=self._client, body=body),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )


class SourcesClient:
    def __init__(self, client: AuthenticatedClient, retry_config: RetryConfig):
        self._client = client
        self._retry_config = retry_config

    def create(self, payload: dict[str, Any]) -> Any:
        body = SourceCreateRequest.from_dict(payload)
        return call_with_retries(
            lambda: create_source_v2_sources_post.sync(client=self._client, body=body),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def list(
        self,
        *,
        type: str | None = None,
        query: str | None = None,
        status: str | None = None,
        category_id: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Any:
        return call_with_retries(
            lambda: list_sources_v2_sources_get.sync(
                client=self._client,
                type=type,
                query=query,
                status=status,
                category_id=category_id,
                limit=limit,
                offset=offset,
            ),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def resolve(self, *, identifier: str, type: str | None = None) -> Any:
        return call_with_retries(
            lambda: resolve_source_v2_sources_resolve_get.sync(
                client=self._client,
                identifier=identifier,
                type=type,
            ),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def get(self, *, source_id: str, type: str | None = None) -> Any:
        return call_with_retries(
            lambda: get_source_v2_sources_source_id_get.sync(
                source_id=source_id,
                client=self._client,
                type=type,
            ),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def delete(self, *, source_id: str, type: str | None = None) -> Any:
        return call_with_retries(
            lambda: delete_source_v2_sources_source_id_delete.sync(
                source_id=source_id,
                client=self._client,
                type=type,
            ),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )


class OracleClient:
    def __init__(self, client: AuthenticatedClient, retry_config: RetryConfig):
        self._client = client
        self._retry_config = retry_config

    def create_job(self, *, query: str, **kwargs: Any) -> Any:
        body = OracleResearchRequest(query=query, **kwargs)
        return call_with_retries(
            lambda: create_oracle_job_v2_oracle_jobs_post.sync(client=self._client, body=body),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def get_job(self, *, job_id: str) -> Any:
        return call_with_retries(
            lambda: get_oracle_job_v2_oracle_jobs_job_id_get.sync(job_id=job_id, client=self._client),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def list_jobs(self, *, status: str | None = None, limit: int = 20, skip: int = 0) -> Any:
        return call_with_retries(
            lambda: list_oracle_jobs_v2_oracle_jobs_get.sync(
                client=self._client,
                status=status,
                limit=limit,
                skip=skip,
            ),
            max_retries=self._retry_config.max_retries,
            initial_backoff_seconds=self._retry_config.initial_backoff_seconds,
        )

    def wait_for_job(
        self,
        *,
        job_id: str,
        timeout_seconds: float = 600.0,
        poll_interval_seconds: float = 2.0,
    ) -> Any:
        deadline = time.time() + timeout_seconds
        while time.time() < deadline:
            job = self.get_job(job_id=job_id)
            status = (job or {}).get("status")
            if status in TERMINAL_JOB_STATUSES:
                return job
            time.sleep(poll_interval_seconds)
        raise NiaTimeoutError(f"Oracle job {job_id} did not reach terminal state within {timeout_seconds}s")

    def stream_job_events(self, *, job_id: str) -> Generator[dict[str, Any], None, None]:
        http_client = self._client.get_httpx_client()
        with http_client.stream("GET", f"/oracle/jobs/{job_id}/stream") as response:
            response.raise_for_status()
            for raw_line in response.iter_lines():
                if not raw_line or not raw_line.startswith("data: "):
                    continue
                payload = raw_line.removeprefix("data: ").strip()
                if not payload:
                    continue
                try:
                    yield json.loads(payload)
                except json.JSONDecodeError:
                    continue


class NiaSDK:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = "https://apigcp.trynia.ai/v2",
        timeout_seconds: float = 60.0,
        max_retries: int = 2,
        initial_backoff_seconds: float = 0.5,
    ):
        self._client = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=httpx.Timeout(timeout_seconds),
            raise_on_unexpected_status=True,
        )
        retry_config = RetryConfig(
            max_retries=max_retries,
            initial_backoff_seconds=initial_backoff_seconds,
        )
        self.search = SearchClient(self._client, retry_config)
        self.sources = SourcesClient(self._client, retry_config)
        self.oracle = OracleClient(self._client, retry_config)
