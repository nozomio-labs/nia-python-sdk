from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.load_vault_v2_vaults_vault_id_load_get_response_load_vault_v2_vaults_vault_id_load_get import (
    LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vault_id: str,
    *,
    paths_only: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["paths_only"] = paths_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vaults/{vault_id}/load".format(
            vault_id=quote(str(vault_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet | None:
    if response.status_code == 200:
        response_200 = LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet.from_dict(response.json())

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
) -> Response[HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    paths_only: bool | Unset = False,
) -> Response[HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet]:
    """Load Vault

     Bootstrap dump for the `nia vault open` bash session.

    Mirrors the shape of /shell-docs/load. Returns vault metadata and either
    full file contents or just paths (for vaults > 1000 files).

    Up to 10000 files are returned (matches DIR_LISTING_LIMIT in fs_service.py).

    Args:
        vault_id (str):
        paths_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
        paths_only=paths_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    paths_only: bool | Unset = False,
) -> HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet | None:
    """Load Vault

     Bootstrap dump for the `nia vault open` bash session.

    Mirrors the shape of /shell-docs/load. Returns vault metadata and either
    full file contents or just paths (for vaults > 1000 files).

    Up to 10000 files are returned (matches DIR_LISTING_LIMIT in fs_service.py).

    Args:
        vault_id (str):
        paths_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet
    """

    return sync_detailed(
        vault_id=vault_id,
        client=client,
        paths_only=paths_only,
    ).parsed


async def asyncio_detailed(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    paths_only: bool | Unset = False,
) -> Response[HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet]:
    """Load Vault

     Bootstrap dump for the `nia vault open` bash session.

    Mirrors the shape of /shell-docs/load. Returns vault metadata and either
    full file contents or just paths (for vaults > 1000 files).

    Up to 10000 files are returned (matches DIR_LISTING_LIMIT in fs_service.py).

    Args:
        vault_id (str):
        paths_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
        paths_only=paths_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
    paths_only: bool | Unset = False,
) -> HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet | None:
    """Load Vault

     Bootstrap dump for the `nia vault open` bash session.

    Mirrors the shape of /shell-docs/load. Returns vault metadata and either
    full file contents or just paths (for vaults > 1000 files).

    Up to 10000 files are returned (matches DIR_LISTING_LIMIT in fs_service.py).

    Args:
        vault_id (str):
        paths_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LoadVaultV2VaultsVaultIdLoadGetResponseLoadVaultV2VaultsVaultIdLoadGet
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            client=client,
            paths_only=paths_only,
        )
    ).parsed
