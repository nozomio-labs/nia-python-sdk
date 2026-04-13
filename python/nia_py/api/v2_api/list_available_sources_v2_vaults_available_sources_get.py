from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_available_sources_v2_vaults_available_sources_get_response_list_available_sources_v2_vaults_available_sources_get import (
    ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vaults/available-sources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
    | None
):
    if response.status_code == 200:
        response_200 = ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet.from_dict(
            response.json()
        )

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
) -> Response[
    HTTPValidationError
    | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[
    HTTPValidationError
    | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
]:
    """List Available Sources

     Return every source the user can add to a vault.

    Merges data_sources (excluding vaults), local_folders, and projects into a
    single list with a unified shape so the frontend picker shows everything.

    Args:
        q (None | str | Unset): Search filter on display_name / url
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet]
    """

    kwargs = _get_kwargs(
        q=q,
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
    q: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> (
    HTTPValidationError
    | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
    | None
):
    """List Available Sources

     Return every source the user can add to a vault.

    Merges data_sources (excluding vaults), local_folders, and projects into a
    single list with a unified shape so the frontend picker shows everything.

    Args:
        q (None | str | Unset): Search filter on display_name / url
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[
    HTTPValidationError
    | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
]:
    """List Available Sources

     Return every source the user can add to a vault.

    Merges data_sources (excluding vaults), local_folders, and projects into a
    single list with a unified shape so the frontend picker shows everything.

    Args:
        q (None | str | Unset): Search filter on display_name / url
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> (
    HTTPValidationError
    | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
    | None
):
    """List Available Sources

     Return every source the user can add to a vault.

    Merges data_sources (excluding vaults), local_folders, and projects into a
    single list with a unified shape so the frontend picker shows everything.

    Args:
        q (None | str | Unset): Search filter on display_name / url
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAvailableSourcesV2VaultsAvailableSourcesGetResponseListAvailableSourcesV2VaultsAvailableSourcesGet
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
            offset=offset,
        )
    ).parsed
