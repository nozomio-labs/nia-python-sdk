from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_vault_source_v2_vaults_vault_id_sources_post_response_add_vault_source_v2_vaults_vault_id_sources_post import (
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    vault_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vaults/{vault_id}/sources".format(
            vault_id=quote(str(vault_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = (
            AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost.from_dict(
                response.json()
            )
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
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError
]:
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
) -> Response[
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError
]:
    """Add Vault Source

     Add a source to the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost
    | HTTPValidationError
    | None
):
    """Add Vault Source

     Add a source to the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError
    """

    return sync_detailed(
        vault_id=vault_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError
]:
    """Add Vault Source

     Add a source to the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost
    | HTTPValidationError
    | None
):
    """Add Vault Source

     Add a source to the vault's source_ids[]. Idempotent.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddVaultSourceV2VaultsVaultIdSourcesPostResponseAddVaultSourceV2VaultsVaultIdSourcesPost | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            client=client,
        )
    ).parsed
