from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_sources_v2_sources_get_type_type_0 import ListSourcesV2SourcesGetTypeType0
from ...models.source_list_response import SourceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: ListSourcesV2SourcesGetTypeType0 | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, ListSourcesV2SourcesGetTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_category_id: None | str | Unset
    if isinstance(category_id, Unset):
        json_category_id = UNSET
    else:
        json_category_id = category_id
    params["category_id"] = json_category_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SourceListResponse | None:
    if response.status_code == 200:
        response_200 = SourceListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SourceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListSourcesV2SourcesGetTypeType0 | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | SourceListResponse]:
    """List Sources

    Args:
        type_ (ListSourcesV2SourcesGetTypeType0 | None | Unset): Filter by source type
        query (None | str | Unset): Search by name or identifier
        status (None | str | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SourceListResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        query=query,
        status=status,
        category_id=category_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: ListSourcesV2SourcesGetTypeType0 | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> HTTPValidationError | SourceListResponse | None:
    """List Sources

    Args:
        type_ (ListSourcesV2SourcesGetTypeType0 | None | Unset): Filter by source type
        query (None | str | Unset): Search by name or identifier
        status (None | str | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SourceListResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
        query=query,
        status=status,
        category_id=category_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListSourcesV2SourcesGetTypeType0 | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | SourceListResponse]:
    """List Sources

    Args:
        type_ (ListSourcesV2SourcesGetTypeType0 | None | Unset): Filter by source type
        query (None | str | Unset): Search by name or identifier
        status (None | str | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SourceListResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        query=query,
        status=status,
        category_id=category_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: ListSourcesV2SourcesGetTypeType0 | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> HTTPValidationError | SourceListResponse | None:
    """List Sources

    Args:
        type_ (ListSourcesV2SourcesGetTypeType0 | None | Unset): Filter by source type
        query (None | str | Unset): Search by name or identifier
        status (None | str | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SourceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            query=query,
            status=status,
            category_id=category_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
