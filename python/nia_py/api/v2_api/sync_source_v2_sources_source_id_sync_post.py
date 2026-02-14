from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sync_source_v2_sources_source_id_sync_post_body import SyncSourceV2SourcesSourceIdSyncPostBody
from ...models.sync_source_v2_sources_source_id_sync_post_type_type_0 import (
    SyncSourceV2SourcesSourceIdSyncPostTypeType0,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_id: str,
    *,
    body: SyncSourceV2SourcesSourceIdSyncPostBody,
    type_: None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, SyncSourceV2SourcesSourceIdSyncPostTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources/{source_id}/sync".format(
            source_id=quote(str(source_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: SyncSourceV2SourcesSourceIdSyncPostBody,
    type_: None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Sync Source

    Args:
        source_id (str):
        type_ (None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset): Source type hint
        body (SyncSourceV2SourcesSourceIdSyncPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        body=body,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncSourceV2SourcesSourceIdSyncPostBody,
    type_: None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Sync Source

    Args:
        source_id (str):
        type_ (None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset): Source type hint
        body (SyncSourceV2SourcesSourceIdSyncPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
        body=body,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncSourceV2SourcesSourceIdSyncPostBody,
    type_: None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Sync Source

    Args:
        source_id (str):
        type_ (None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset): Source type hint
        body (SyncSourceV2SourcesSourceIdSyncPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        body=body,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncSourceV2SourcesSourceIdSyncPostBody,
    type_: None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Sync Source

    Args:
        source_id (str):
        type_ (None | SyncSourceV2SourcesSourceIdSyncPostTypeType0 | Unset): Source type hint
        body (SyncSourceV2SourcesSourceIdSyncPostBody):

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
            body=body,
            type_=type_,
        )
    ).parsed
