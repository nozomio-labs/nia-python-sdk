from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    ref: str | Unset = "HEAD",
    path: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ref"] = ref

    json_path: None | str | Unset
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/github/tree/{owner}/{repo}".format(
            owner=quote(str(owner), safe=""),
            repo=quote(str(repo), safe=""),
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
    owner: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = "HEAD",
    path: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Github Tree

     Get the file tree of a GitHub repository or subdirectory.

    Args:
        owner (str):
        repo (str):
        ref (str | Unset): Branch, tag, or commit SHA Default: 'HEAD'.
        path (None | str | Unset): Subdirectory path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        ref=ref,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    owner: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = "HEAD",
    path: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Github Tree

     Get the file tree of a GitHub repository or subdirectory.

    Args:
        owner (str):
        repo (str):
        ref (str | Unset): Branch, tag, or commit SHA Default: 'HEAD'.
        path (None | str | Unset): Subdirectory path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        client=client,
        ref=ref,
        path=path,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = "HEAD",
    path: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Github Tree

     Get the file tree of a GitHub repository or subdirectory.

    Args:
        owner (str):
        repo (str):
        ref (str | Unset): Branch, tag, or commit SHA Default: 'HEAD'.
        path (None | str | Unset): Subdirectory path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        ref=ref,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    owner: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = "HEAD",
    path: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Github Tree

     Get the file tree of a GitHub repository or subdirectory.

    Args:
        owner (str):
        repo (str):
        ref (str | Unset): Branch, tag, or commit SHA Default: 'HEAD'.
        path (None | str | Unset): Subdirectory path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
            ref=ref,
            path=path,
        )
    ).parsed
