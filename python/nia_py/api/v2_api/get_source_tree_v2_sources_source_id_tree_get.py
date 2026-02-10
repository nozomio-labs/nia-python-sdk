from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_source_tree_v2_sources_source_id_tree_get_type_type_0 import (
    GetSourceTreeV2SourcesSourceIdTreeGetTypeType0,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_id: str,
    *,
    type_: GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset = UNSET,
    branch: None | str | Unset = UNSET,
    max_depth: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, GetSourceTreeV2SourcesSourceIdTreeGetTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_branch: None | str | Unset
    if isinstance(branch, Unset):
        json_branch = UNSET
    else:
        json_branch = branch
    params["branch"] = json_branch

    params["max_depth"] = max_depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/{source_id}/tree".format(
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
    type_: GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset = UNSET,
    branch: None | str | Unset = UNSET,
    max_depth: int | Unset = 10,
) -> Response[Any | HTTPValidationError]:
    """Get Source Tree

    Args:
        source_id (str):
        type_ (GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset): Source type hint
        branch (None | str | Unset): Repository branch
        max_depth (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        type_=type_,
        branch=branch,
        max_depth=max_depth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset = UNSET,
    branch: None | str | Unset = UNSET,
    max_depth: int | Unset = 10,
) -> Any | HTTPValidationError | None:
    """Get Source Tree

    Args:
        source_id (str):
        type_ (GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset): Source type hint
        branch (None | str | Unset): Repository branch
        max_depth (int | Unset):  Default: 10.

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
        branch=branch,
        max_depth=max_depth,
    ).parsed


async def asyncio_detailed(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset = UNSET,
    branch: None | str | Unset = UNSET,
    max_depth: int | Unset = 10,
) -> Response[Any | HTTPValidationError]:
    """Get Source Tree

    Args:
        source_id (str):
        type_ (GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset): Source type hint
        branch (None | str | Unset): Repository branch
        max_depth (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        type_=type_,
        branch=branch,
        max_depth=max_depth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset = UNSET,
    branch: None | str | Unset = UNSET,
    max_depth: int | Unset = 10,
) -> Any | HTTPValidationError | None:
    """Get Source Tree

    Args:
        source_id (str):
        type_ (GetSourceTreeV2SourcesSourceIdTreeGetTypeType0 | None | Unset): Source type hint
        branch (None | str | Unset): Repository branch
        max_depth (int | Unset):  Default: 10.

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
            branch=branch,
            max_depth=max_depth,
        )
    ).parsed
