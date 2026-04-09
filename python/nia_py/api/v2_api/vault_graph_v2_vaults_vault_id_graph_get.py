from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.vault_graph_v2_vaults_vault_id_graph_get_response_vault_graph_v2_vaults_vault_id_graph_get import (
    VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet,
)
from ...types import Response


def _get_kwargs(
    vault_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vaults/{vault_id}/graph".format(
            vault_id=quote(str(vault_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet | None:
    if response.status_code == 200:
        response_200 = VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet.from_dict(
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
) -> Response[HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet]:
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
) -> Response[HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet]:
    """Vault Graph

     Return the wikilink graph as nodes + edges for visualization.

    Walks all concept/entity/note pages, parses [[wikilinks]], and builds a
    force-directed-ready JSON structure. No LLM calls — pure file parsing.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet]
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
) -> HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet | None:
    """Vault Graph

     Return the wikilink graph as nodes + edges for visualization.

    Walks all concept/entity/note pages, parses [[wikilinks]], and builds a
    force-directed-ready JSON structure. No LLM calls — pure file parsing.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet
    """

    return sync_detailed(
        vault_id=vault_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet]:
    """Vault Graph

     Return the wikilink graph as nodes + edges for visualization.

    Walks all concept/entity/note pages, parses [[wikilinks]], and builds a
    force-directed-ready JSON structure. No LLM calls — pure file parsing.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet]
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
) -> HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet | None:
    """Vault Graph

     Return the wikilink graph as nodes + edges for visualization.

    Walks all concept/entity/note pages, parses [[wikilinks]], and builds a
    force-directed-ready JSON structure. No LLM calls — pure file parsing.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            client=client,
        )
    ).parsed
