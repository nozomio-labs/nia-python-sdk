from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    installation_id: str,
    *,
    folder_id: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    page_token: None | str | Unset = UNSET,
    page_size: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_folder_id: None | str | Unset
    if isinstance(folder_id, Unset):
        json_folder_id = UNSET
    else:
        json_folder_id = folder_id
    params["folder_id"] = json_folder_id

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_page_token: None | str | Unset
    if isinstance(page_token, Unset):
        json_page_token = UNSET
    else:
        json_page_token = page_token
    params["page_token"] = json_page_token

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/google-drive/installations/{installation_id}/browse".format(
            installation_id=quote(str(installation_id), safe=""),
        ),
        "params": params,
    }

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
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    folder_id: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    page_token: None | str | Unset = UNSET,
    page_size: int | Unset = 100,
) -> Response[Any | HTTPValidationError]:
    """Browse Google Drive Items

    Args:
        installation_id (str):
        folder_id (None | str | Unset): Optional Drive folder ID to browse
        q (None | str | Unset): Optional Drive item name search
        page_token (None | str | Unset): Pagination token from the previous response
        page_size (int | Unset): Maximum Drive items to return Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        installation_id=installation_id,
        folder_id=folder_id,
        q=q,
        page_token=page_token,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    folder_id: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    page_token: None | str | Unset = UNSET,
    page_size: int | Unset = 100,
) -> Any | HTTPValidationError | None:
    """Browse Google Drive Items

    Args:
        installation_id (str):
        folder_id (None | str | Unset): Optional Drive folder ID to browse
        q (None | str | Unset): Optional Drive item name search
        page_token (None | str | Unset): Pagination token from the previous response
        page_size (int | Unset): Maximum Drive items to return Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        installation_id=installation_id,
        client=client,
        folder_id=folder_id,
        q=q,
        page_token=page_token,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    folder_id: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    page_token: None | str | Unset = UNSET,
    page_size: int | Unset = 100,
) -> Response[Any | HTTPValidationError]:
    """Browse Google Drive Items

    Args:
        installation_id (str):
        folder_id (None | str | Unset): Optional Drive folder ID to browse
        q (None | str | Unset): Optional Drive item name search
        page_token (None | str | Unset): Pagination token from the previous response
        page_size (int | Unset): Maximum Drive items to return Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        installation_id=installation_id,
        folder_id=folder_id,
        q=q,
        page_token=page_token,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    folder_id: None | str | Unset = UNSET,
    q: None | str | Unset = UNSET,
    page_token: None | str | Unset = UNSET,
    page_size: int | Unset = 100,
) -> Any | HTTPValidationError | None:
    """Browse Google Drive Items

    Args:
        installation_id (str):
        folder_id (None | str | Unset): Optional Drive folder ID to browse
        q (None | str | Unset): Optional Drive item name search
        page_token (None | str | Unset): Pagination token from the previous response
        page_size (int | Unset): Maximum Drive items to return Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            installation_id=installation_id,
            client=client,
            folder_id=folder_id,
            q=q,
            page_token=page_token,
            page_size=page_size,
        )
    ).parsed
