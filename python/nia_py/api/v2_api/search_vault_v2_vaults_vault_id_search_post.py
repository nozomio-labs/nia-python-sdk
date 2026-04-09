from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.search_vault_v2_vaults_vault_id_search_post_response_search_vault_v2_vaults_vault_id_search_post import (
    SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost,
)
from ...types import Response


def _get_kwargs(
    vault_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vaults/{vault_id}/search".format(
            vault_id=quote(str(vault_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost | None:
    if response.status_code == 200:
        response_200 = SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost.from_dict(
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
) -> Response[HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost]:
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
) -> Response[HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost]:
    """Search Vault

     Hybrid search scoped to this vault's namespace.

    Returns embedded vault pages as ranked results with citations. The vault
    namespace was populated by the existing `fs_sync_workflow` mirroring every
    write into TurboPuffer (see routes/v2/fs.py:294-313).

    Telemetry: emits both `store_api_activity` (for the user-facing activity
    feed) and `store_retrieval_log` (for the training-data pipeline) so vault
    searches show up alongside every other retrieval call. Two retrieval logs
    are written for the two-tier strategy: a `vector` log for the TurboPuffer
    path, and a `regex` log if the PG grep fallback fires.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost]
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
) -> HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost | None:
    """Search Vault

     Hybrid search scoped to this vault's namespace.

    Returns embedded vault pages as ranked results with citations. The vault
    namespace was populated by the existing `fs_sync_workflow` mirroring every
    write into TurboPuffer (see routes/v2/fs.py:294-313).

    Telemetry: emits both `store_api_activity` (for the user-facing activity
    feed) and `store_retrieval_log` (for the training-data pipeline) so vault
    searches show up alongside every other retrieval call. Two retrieval logs
    are written for the two-tier strategy: a `vector` log for the TurboPuffer
    path, and a `regex` log if the PG grep fallback fires.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost
    """

    return sync_detailed(
        vault_id=vault_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost]:
    """Search Vault

     Hybrid search scoped to this vault's namespace.

    Returns embedded vault pages as ranked results with citations. The vault
    namespace was populated by the existing `fs_sync_workflow` mirroring every
    write into TurboPuffer (see routes/v2/fs.py:294-313).

    Telemetry: emits both `store_api_activity` (for the user-facing activity
    feed) and `store_retrieval_log` (for the training-data pipeline) so vault
    searches show up alongside every other retrieval call. Two retrieval logs
    are written for the two-tier strategy: a `vector` log for the TurboPuffer
    path, and a `regex` log if the PG grep fallback fires.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost]
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
) -> HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost | None:
    """Search Vault

     Hybrid search scoped to this vault's namespace.

    Returns embedded vault pages as ranked results with citations. The vault
    namespace was populated by the existing `fs_sync_workflow` mirroring every
    write into TurboPuffer (see routes/v2/fs.py:294-313).

    Telemetry: emits both `store_api_activity` (for the user-facing activity
    feed) and `store_retrieval_log` (for the training-data pipeline) so vault
    searches show up alongside every other retrieval call. Two retrieval logs
    are written for the two-tier strategy: a `vector` log for the TurboPuffer
    path, and a `regex` log if the PG grep fallback fires.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SearchVaultV2VaultsVaultIdSearchPostResponseSearchVaultV2VaultsVaultIdSearchPost
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            client=client,
        )
    ).parsed
