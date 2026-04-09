from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_vault_v2_vaults_post_response_create_vault_v2_vaults_post import (
    CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vaults",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost | None:
    if response.status_code == 200:
        response_200 = CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost]:
    """Create Vault

     Create a new vault.

    Body: {display_name: str, description?: str, source_ids?: [str], schema_md?: str}

    Bootstraps the vault namespace with schema.md/index.md/log.md/META.md.
    Does NOT auto-trigger ingest — call POST /v2/vaults/{id}/run with
    mode=ingest after creation if you want immediate ingestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost | None:
    """Create Vault

     Create a new vault.

    Body: {display_name: str, description?: str, source_ids?: [str], schema_md?: str}

    Bootstraps the vault namespace with schema.md/index.md/log.md/META.md.
    Does NOT auto-trigger ingest — call POST /v2/vaults/{id}/run with
    mode=ingest after creation if you want immediate ingestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost]:
    """Create Vault

     Create a new vault.

    Body: {display_name: str, description?: str, source_ids?: [str], schema_md?: str}

    Bootstraps the vault namespace with schema.md/index.md/log.md/META.md.
    Does NOT auto-trigger ingest — call POST /v2/vaults/{id}/run with
    mode=ingest after creation if you want immediate ingestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost | None:
    """Create Vault

     Create a new vault.

    Body: {display_name: str, description?: str, source_ids?: [str], schema_md?: str}

    Bootstraps the vault namespace with schema.md/index.md/log.md/META.md.
    Does NOT auto-trigger ingest — call POST /v2/vaults/{id}/run with
    mode=ingest after creation if you want immediate ingestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVaultV2VaultsPostResponseCreateVaultV2VaultsPost
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
