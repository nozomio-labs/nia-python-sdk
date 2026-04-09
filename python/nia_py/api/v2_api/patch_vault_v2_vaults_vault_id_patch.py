from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.patch_vault_v2_vaults_vault_id_patch_response_patch_vault_v2_vaults_vault_id_patch import (
    PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch,
)
from ...types import Response


def _get_kwargs(
    vault_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/vaults/{vault_id}".format(
            vault_id=quote(str(vault_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch | None:
    if response.status_code == 200:
        response_200 = PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch.from_dict(response.json())

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
) -> Response[HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch]:
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
) -> Response[HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch]:
    """Patch Vault

     Update vault metadata (display_name, description, schema_md).

    When schema_md is updated, the new content is also written into the
    vault namespace as `/schema.md` so the bash session sees it immediately.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch]
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
) -> HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch | None:
    """Patch Vault

     Update vault metadata (display_name, description, schema_md).

    When schema_md is updated, the new content is also written into the
    vault namespace as `/schema.md` so the bash session sees it immediately.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch
    """

    return sync_detailed(
        vault_id=vault_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vault_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch]:
    """Patch Vault

     Update vault metadata (display_name, description, schema_md).

    When schema_md is updated, the new content is also written into the
    vault namespace as `/schema.md` so the bash session sees it immediately.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch]
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
) -> HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch | None:
    """Patch Vault

     Update vault metadata (display_name, description, schema_md).

    When schema_md is updated, the new content is also written into the
    vault namespace as `/schema.md` so the bash session sees it immediately.

    Args:
        vault_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PatchVaultV2VaultsVaultIdPatchResponsePatchVaultV2VaultsVaultIdPatch
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            client=client,
        )
    ).parsed
