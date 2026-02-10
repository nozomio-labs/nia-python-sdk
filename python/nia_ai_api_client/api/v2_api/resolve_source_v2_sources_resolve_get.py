from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.resolve_source_v2_sources_resolve_get_type_type_0 import ResolveSourceV2SourcesResolveGetTypeType0
from ...models.source_resolve_response import SourceResolveResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identifier: str,
    type_: None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identifier"] = identifier

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, ResolveSourceV2SourcesResolveGetTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/resolve",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SourceResolveResponse | None:
    if response.status_code == 200:
        response_200 = SourceResolveResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SourceResolveResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    type_: None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset = UNSET,
) -> Response[HTTPValidationError | SourceResolveResponse]:
    """Resolve Source

    Args:
        identifier (str): Display name, URL, or slug
        type_ (None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset): Source type hint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SourceResolveResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    type_: None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset = UNSET,
) -> HTTPValidationError | SourceResolveResponse | None:
    """Resolve Source

    Args:
        identifier (str): Display name, URL, or slug
        type_ (None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset): Source type hint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SourceResolveResponse
    """

    return sync_detailed(
        client=client,
        identifier=identifier,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    type_: None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset = UNSET,
) -> Response[HTTPValidationError | SourceResolveResponse]:
    """Resolve Source

    Args:
        identifier (str): Display name, URL, or slug
        type_ (None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset): Source type hint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SourceResolveResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    type_: None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset = UNSET,
) -> HTTPValidationError | SourceResolveResponse | None:
    """Resolve Source

    Args:
        identifier (str): Display name, URL, or slug
        type_ (None | ResolveSourceV2SourcesResolveGetTypeType0 | Unset): Source type hint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SourceResolveResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            identifier=identifier,
            type_=type_,
        )
    ).parsed
