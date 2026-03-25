from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_response import ExtractResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    extraction_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/extract/{extraction_id}".format(
            extraction_id=quote(str(extraction_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExtractResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExtractResponse.from_dict(response.json())

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
) -> Response[ExtractResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    extraction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExtractResponse | HTTPValidationError]:
    """Get Extraction

    Args:
        extraction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        extraction_id=extraction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extraction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExtractResponse | HTTPValidationError | None:
    """Get Extraction

    Args:
        extraction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtractResponse | HTTPValidationError
    """

    return sync_detailed(
        extraction_id=extraction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    extraction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExtractResponse | HTTPValidationError]:
    """Get Extraction

    Args:
        extraction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        extraction_id=extraction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extraction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExtractResponse | HTTPValidationError | None:
    """Get Extraction

    Args:
        extraction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtractResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            extraction_id=extraction_id,
            client=client,
        )
    ).parsed
