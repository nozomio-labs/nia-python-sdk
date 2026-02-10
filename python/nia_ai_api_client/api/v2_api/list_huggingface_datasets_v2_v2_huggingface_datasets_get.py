from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.hugging_face_dataset_list_response import HuggingFaceDatasetListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    organization_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset

    json_organization_id: None | str | Unset
    if isinstance(organization_id, Unset):
        json_organization_id = UNSET
    else:
        json_organization_id = organization_id
    params["organization_id"] = json_organization_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/huggingface-datasets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | HuggingFaceDatasetListResponse | None:
    if response.status_code == 200:
        response_200 = HuggingFaceDatasetListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | HuggingFaceDatasetListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    organization_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | HuggingFaceDatasetListResponse]:
    """List HuggingFace datasets

     List all indexed HuggingFace datasets with metadata.

    Args:
        status (None | str | Unset): Filter by status: processing, completed, failed
        limit (int | Unset): Maximum number of results Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
        organization_id (None | str | Unset): Organization ID for org-level filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | HuggingFaceDatasetListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        offset=offset,
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    organization_id: None | str | Unset = UNSET,
) -> HTTPValidationError | HuggingFaceDatasetListResponse | None:
    """List HuggingFace datasets

     List all indexed HuggingFace datasets with metadata.

    Args:
        status (None | str | Unset): Filter by status: processing, completed, failed
        limit (int | Unset): Maximum number of results Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
        organization_id (None | str | Unset): Organization ID for org-level filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | HuggingFaceDatasetListResponse
    """

    return sync_detailed(
        client=client,
        status=status,
        limit=limit,
        offset=offset,
        organization_id=organization_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    organization_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | HuggingFaceDatasetListResponse]:
    """List HuggingFace datasets

     List all indexed HuggingFace datasets with metadata.

    Args:
        status (None | str | Unset): Filter by status: processing, completed, failed
        limit (int | Unset): Maximum number of results Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
        organization_id (None | str | Unset): Organization ID for org-level filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | HuggingFaceDatasetListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        offset=offset,
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    organization_id: None | str | Unset = UNSET,
) -> HTTPValidationError | HuggingFaceDatasetListResponse | None:
    """List HuggingFace datasets

     List all indexed HuggingFace datasets with metadata.

    Args:
        status (None | str | Unset): Filter by status: processing, completed, failed
        limit (int | Unset): Maximum number of results Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
        organization_id (None | str | Unset): Organization ID for org-level filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | HuggingFaceDatasetListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            limit=limit,
            offset=offset,
            organization_id=organization_id,
        )
    ).parsed
