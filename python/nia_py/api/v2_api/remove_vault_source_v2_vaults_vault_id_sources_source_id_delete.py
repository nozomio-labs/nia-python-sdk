from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.remove_vault_source_v2_vaults_vault_id_sources_source_id_delete_response_remove_vault_source_v2_vaults_vault_id_sources_source_id_delete import (
    RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete,
)
from ...types import Response


def _get_kwargs(
    vault_id: str,
    source_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/vaults/{vault_id}/sources/{source_id}".format(
            vault_id=quote(str(vault_id), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
    | None
):
    if response.status_code == 200:
        response_200 = RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete.from_dict(
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
    | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vault_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    HTTPValidationError
    | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
]:
    """Remove Vault Source

     Remove a source from the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
        source_id=source_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vault_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    HTTPValidationError
    | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
    | None
):
    """Remove Vault Source

     Remove a source from the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
    """

    return sync_detailed(
        vault_id=vault_id,
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vault_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    HTTPValidationError
    | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
]:
    """Remove Vault Source

     Remove a source from the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
        source_id=source_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vault_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    HTTPValidationError
    | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
    | None
):
    """Remove Vault Source

     Remove a source from the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDeleteResponseRemoveVaultSourceV2VaultsVaultIdSourcesSourceIdDelete
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            source_id=source_id,
            client=client,
        )
    ).parsed
