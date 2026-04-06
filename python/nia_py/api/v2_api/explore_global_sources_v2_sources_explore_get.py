from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: str | Unset = "",
    source_type: str | Unset = "",
    status: str | Unset = "indexed",
    sort: str | Unset = "most_subscribed",
    order: str | Unset = "desc",
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    params["source_type"] = source_type

    params["status"] = status

    params["sort"] = sort

    params["order"] = order

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/explore",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = "",
    source_type: str | Unset = "",
    status: str | Unset = "indexed",
    sort: str | Unset = "most_subscribed",
    order: str | Unset = "desc",
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[Any | HTTPValidationError]:
    """Explore Global Sources

     Browse the global catalog of publicly indexed sources.

    Args:
        search (str | Unset): Search by URL or name Default: ''.
        source_type (str | Unset): Filter by type: repository | documentation | research_paper |
            huggingface_dataset Default: ''.
        status (str | Unset): Filter by status Default: 'indexed'.
        sort (str | Unset): Sort: recently_indexed | recently_updated | most_tokens |
            most_snippets | most_subscribed | relevance Default: 'most_subscribed'.
        order (str | Unset): Sort direction: asc | desc Default: 'desc'.
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        source_type=source_type,
        status=status,
        sort=sort,
        order=order,
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
    search: str | Unset = "",
    source_type: str | Unset = "",
    status: str | Unset = "indexed",
    sort: str | Unset = "most_subscribed",
    order: str | Unset = "desc",
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Any | HTTPValidationError | None:
    """Explore Global Sources

     Browse the global catalog of publicly indexed sources.

    Args:
        search (str | Unset): Search by URL or name Default: ''.
        source_type (str | Unset): Filter by type: repository | documentation | research_paper |
            huggingface_dataset Default: ''.
        status (str | Unset): Filter by status Default: 'indexed'.
        sort (str | Unset): Sort: recently_indexed | recently_updated | most_tokens |
            most_snippets | most_subscribed | relevance Default: 'most_subscribed'.
        order (str | Unset): Sort direction: asc | desc Default: 'desc'.
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        search=search,
        source_type=source_type,
        status=status,
        sort=sort,
        order=order,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = "",
    source_type: str | Unset = "",
    status: str | Unset = "indexed",
    sort: str | Unset = "most_subscribed",
    order: str | Unset = "desc",
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[Any | HTTPValidationError]:
    """Explore Global Sources

     Browse the global catalog of publicly indexed sources.

    Args:
        search (str | Unset): Search by URL or name Default: ''.
        source_type (str | Unset): Filter by type: repository | documentation | research_paper |
            huggingface_dataset Default: ''.
        status (str | Unset): Filter by status Default: 'indexed'.
        sort (str | Unset): Sort: recently_indexed | recently_updated | most_tokens |
            most_snippets | most_subscribed | relevance Default: 'most_subscribed'.
        order (str | Unset): Sort direction: asc | desc Default: 'desc'.
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        source_type=source_type,
        status=status,
        sort=sort,
        order=order,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = "",
    source_type: str | Unset = "",
    status: str | Unset = "indexed",
    sort: str | Unset = "most_subscribed",
    order: str | Unset = "desc",
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Any | HTTPValidationError | None:
    """Explore Global Sources

     Browse the global catalog of publicly indexed sources.

    Args:
        search (str | Unset): Search by URL or name Default: ''.
        source_type (str | Unset): Filter by type: repository | documentation | research_paper |
            huggingface_dataset Default: ''.
        status (str | Unset): Filter by status Default: 'indexed'.
        sort (str | Unset): Sort: recently_indexed | recently_updated | most_tokens |
            most_snippets | most_subscribed | relevance Default: 'most_subscribed'.
        order (str | Unset): Sort direction: asc | desc Default: 'desc'.
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            source_type=source_type,
            status=status,
            sort=sort,
            order=order,
            limit=limit,
            offset=offset,
        )
    ).parsed
