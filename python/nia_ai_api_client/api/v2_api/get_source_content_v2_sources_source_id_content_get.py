from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_source_content_v2_sources_source_id_content_get_type_type_0 import (
    GetSourceContentV2SourcesSourceIdContentGetTypeType0,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_id: str,
    *,
    type_: GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset = UNSET,
    path: None | str | Unset = UNSET,
    url_query: None | str | Unset = UNSET,
    branch: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, GetSourceContentV2SourcesSourceIdContentGetTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_path: None | str | Unset
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    json_url_query: None | str | Unset
    if isinstance(url_query, Unset):
        json_url_query = UNSET
    else:
        json_url_query = url_query
    params["url"] = json_url_query

    json_branch: None | str | Unset
    if isinstance(branch, Unset):
        json_branch = UNSET
    else:
        json_branch = branch
    params["branch"] = json_branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/{source_id}/content".format(
            source_id=quote(str(source_id), safe=""),
        ),
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
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset = UNSET,
    path: None | str | Unset = UNSET,
    url_query: None | str | Unset = UNSET,
    branch: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Source Content

    Args:
        source_id (str):
        type_ (GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset): Source type
            hint
        path (None | str | Unset): Path or virtual path
        url_query (None | str | Unset): Direct URL (documentation)
        branch (None | str | Unset): Repository branch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        type_=type_,
        path=path,
        url_query=url_query,
        branch=branch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset = UNSET,
    path: None | str | Unset = UNSET,
    url_query: None | str | Unset = UNSET,
    branch: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Source Content

    Args:
        source_id (str):
        type_ (GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset): Source type
            hint
        path (None | str | Unset): Path or virtual path
        url_query (None | str | Unset): Direct URL (documentation)
        branch (None | str | Unset): Repository branch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
        type_=type_,
        path=path,
        url_query=url_query,
        branch=branch,
    ).parsed


async def asyncio_detailed(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset = UNSET,
    path: None | str | Unset = UNSET,
    url_query: None | str | Unset = UNSET,
    branch: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Source Content

    Args:
        source_id (str):
        type_ (GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset): Source type
            hint
        path (None | str | Unset): Path or virtual path
        url_query (None | str | Unset): Direct URL (documentation)
        branch (None | str | Unset): Repository branch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        type_=type_,
        path=path,
        url_query=url_query,
        branch=branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset = UNSET,
    path: None | str | Unset = UNSET,
    url_query: None | str | Unset = UNSET,
    branch: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Source Content

    Args:
        source_id (str):
        type_ (GetSourceContentV2SourcesSourceIdContentGetTypeType0 | None | Unset): Source type
            hint
        path (None | str | Unset): Path or virtual path
        url_query (None | str | Unset): Direct URL (documentation)
        branch (None | str | Unset): Repository branch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            client=client,
            type_=type_,
            path=path,
            url_query=url_query,
            branch=branch,
        )
    ).parsed
