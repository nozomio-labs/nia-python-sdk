from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_agent_job_response import DocumentAgentJobResponse
from ...models.document_query_request import DocumentQueryRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: DocumentQueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/document/agent/jobs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentAgentJobResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DocumentAgentJobResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DocumentAgentJobResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DocumentQueryRequest,
) -> Response[DocumentAgentJobResponse | HTTPValidationError]:
    """Enqueue an async document agent job

     Create a long-running document agent job. Returns immediately with a `job_id` — use GET
    /document/agent/jobs/{job_id} to poll for the result or GET /document/agent/jobs/{job_id}/stream for
    live SSE updates.

    Recommended for production workloads, batch evaluation pipelines, or anything that may run longer
    than ~10 minutes. The job runs on a background worker pool with 30-minute hard timeout, per-user
    concurrency caps, and automatic refunds on failure.

    Args:
        body (DocumentQueryRequest): Request for the v2 document/agent endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentAgentJobResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DocumentQueryRequest,
) -> DocumentAgentJobResponse | HTTPValidationError | None:
    """Enqueue an async document agent job

     Create a long-running document agent job. Returns immediately with a `job_id` — use GET
    /document/agent/jobs/{job_id} to poll for the result or GET /document/agent/jobs/{job_id}/stream for
    live SSE updates.

    Recommended for production workloads, batch evaluation pipelines, or anything that may run longer
    than ~10 minutes. The job runs on a background worker pool with 30-minute hard timeout, per-user
    concurrency caps, and automatic refunds on failure.

    Args:
        body (DocumentQueryRequest): Request for the v2 document/agent endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentAgentJobResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DocumentQueryRequest,
) -> Response[DocumentAgentJobResponse | HTTPValidationError]:
    """Enqueue an async document agent job

     Create a long-running document agent job. Returns immediately with a `job_id` — use GET
    /document/agent/jobs/{job_id} to poll for the result or GET /document/agent/jobs/{job_id}/stream for
    live SSE updates.

    Recommended for production workloads, batch evaluation pipelines, or anything that may run longer
    than ~10 minutes. The job runs on a background worker pool with 30-minute hard timeout, per-user
    concurrency caps, and automatic refunds on failure.

    Args:
        body (DocumentQueryRequest): Request for the v2 document/agent endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentAgentJobResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DocumentQueryRequest,
) -> DocumentAgentJobResponse | HTTPValidationError | None:
    """Enqueue an async document agent job

     Create a long-running document agent job. Returns immediately with a `job_id` — use GET
    /document/agent/jobs/{job_id} to poll for the result or GET /document/agent/jobs/{job_id}/stream for
    live SSE updates.

    Recommended for production workloads, batch evaluation pipelines, or anything that may run longer
    than ~10 minutes. The job runs on a background worker pool with 30-minute hard timeout, per-user
    concurrency caps, and automatic refunds on failure.

    Args:
        body (DocumentQueryRequest): Request for the v2 document/agent endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentAgentJobResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
