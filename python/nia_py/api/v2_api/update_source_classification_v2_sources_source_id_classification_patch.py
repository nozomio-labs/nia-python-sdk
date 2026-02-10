from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.classify_local_folder_request import ClassifyLocalFolderRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.update_source_classification_v2_sources_source_id_classification_patch_type_type_0 import (
    UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_id: str,
    *,
    body: ClassifyLocalFolderRequest,
    type_: None | Unset | UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0 = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/sources/{source_id}/classification".format(
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
    body: ClassifyLocalFolderRequest,
    type_: None | Unset | UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0 = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Update Source Classification

    Args:
        source_id (str):
        type_ (None | Unset |
            UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0): Source type hint
        body (ClassifyLocalFolderRequest): Request to classify local folder content.

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
    body: ClassifyLocalFolderRequest,
    type_: None | Unset | UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0 = UNSET,
) -> Any | HTTPValidationError | None:
    """Update Source Classification

    Args:
        source_id (str):
        type_ (None | Unset |
            UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0): Source type hint
        body (ClassifyLocalFolderRequest): Request to classify local folder content.

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
    body: ClassifyLocalFolderRequest,
    type_: None | Unset | UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0 = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Update Source Classification

    Args:
        source_id (str):
        type_ (None | Unset |
            UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0): Source type hint
        body (ClassifyLocalFolderRequest): Request to classify local folder content.

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
    body: ClassifyLocalFolderRequest,
    type_: None | Unset | UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0 = UNSET,
) -> Any | HTTPValidationError | None:
    """Update Source Classification

    Args:
        source_id (str):
        type_ (None | Unset |
            UpdateSourceClassificationV2SourcesSourceIdClassificationPatchTypeType0): Source type hint
        body (ClassifyLocalFolderRequest): Request to classify local folder content.

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
