from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_id: str,
    *,
    path: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
    tree_node_id: None | str | Unset = UNSET,
    line_start: int | None | Unset = UNSET,
    line_end: int | None | Unset = UNSET,
    max_length: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_path: None | str | Unset
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    json_page: int | None | Unset
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    json_tree_node_id: None | str | Unset
    if isinstance(tree_node_id, Unset):
        json_tree_node_id = UNSET
    else:
        json_tree_node_id = tree_node_id
    params["tree_node_id"] = json_tree_node_id

    json_line_start: int | None | Unset
    if isinstance(line_start, Unset):
        json_line_start = UNSET
    else:
        json_line_start = line_start
    params["line_start"] = json_line_start

    json_line_end: int | None | Unset
    if isinstance(line_end, Unset):
        json_line_end = UNSET
    else:
        json_line_end = line_end
    params["line_end"] = json_line_end

    json_max_length: int | None | Unset
    if isinstance(max_length, Unset):
        json_max_length = UNSET
    else:
        json_max_length = max_length
    params["max_length"] = json_max_length

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-sources/{source_id}/read".format(
            source_id=quote(str(source_id), safe=""),
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
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
    tree_node_id: None | str | Unset = UNSET,
    line_start: int | None | Unset = UNSET,
    line_end: int | None | Unset = UNSET,
    max_length: int | None | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Read documentation page

     Read page content by virtual path, page number, or tree node. Supports line range and max_length
    truncation.

    Args:
        source_id (str):
        path (None | str | Unset): Virtual path (for web docs)
        page (int | None | Unset): Page number (for PDFs with tree index)
        tree_node_id (None | str | Unset): Tree node ID (for PDFs with tree index)
        line_start (int | None | Unset): Start line (1-based, inclusive)
        line_end (int | None | Unset): End line (1-based, inclusive)
        max_length (int | None | Unset): Max characters to return

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        path=path,
        page=page,
        tree_node_id=tree_node_id,
        line_start=line_start,
        line_end=line_end,
        max_length=max_length,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
    tree_node_id: None | str | Unset = UNSET,
    line_start: int | None | Unset = UNSET,
    line_end: int | None | Unset = UNSET,
    max_length: int | None | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Read documentation page

     Read page content by virtual path, page number, or tree node. Supports line range and max_length
    truncation.

    Args:
        source_id (str):
        path (None | str | Unset): Virtual path (for web docs)
        page (int | None | Unset): Page number (for PDFs with tree index)
        tree_node_id (None | str | Unset): Tree node ID (for PDFs with tree index)
        line_start (int | None | Unset): Start line (1-based, inclusive)
        line_end (int | None | Unset): End line (1-based, inclusive)
        max_length (int | None | Unset): Max characters to return

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
        path=path,
        page=page,
        tree_node_id=tree_node_id,
        line_start=line_start,
        line_end=line_end,
        max_length=max_length,
    ).parsed


async def asyncio_detailed(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
    tree_node_id: None | str | Unset = UNSET,
    line_start: int | None | Unset = UNSET,
    line_end: int | None | Unset = UNSET,
    max_length: int | None | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Read documentation page

     Read page content by virtual path, page number, or tree node. Supports line range and max_length
    truncation.

    Args:
        source_id (str):
        path (None | str | Unset): Virtual path (for web docs)
        page (int | None | Unset): Page number (for PDFs with tree index)
        tree_node_id (None | str | Unset): Tree node ID (for PDFs with tree index)
        line_start (int | None | Unset): Start line (1-based, inclusive)
        line_end (int | None | Unset): End line (1-based, inclusive)
        max_length (int | None | Unset): Max characters to return

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        path=path,
        page=page,
        tree_node_id=tree_node_id,
        line_start=line_start,
        line_end=line_end,
        max_length=max_length,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
    tree_node_id: None | str | Unset = UNSET,
    line_start: int | None | Unset = UNSET,
    line_end: int | None | Unset = UNSET,
    max_length: int | None | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Read documentation page

     Read page content by virtual path, page number, or tree node. Supports line range and max_length
    truncation.

    Args:
        source_id (str):
        path (None | str | Unset): Virtual path (for web docs)
        page (int | None | Unset): Page number (for PDFs with tree index)
        tree_node_id (None | str | Unset): Tree node ID (for PDFs with tree index)
        line_start (int | None | Unset): Start line (1-based, inclusive)
        line_end (int | None | Unset): End line (1-based, inclusive)
        max_length (int | None | Unset): Max characters to return

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            client=client,
            path=path,
            page=page,
            tree_node_id=tree_node_id,
            line_start=line_start,
            line_end=line_end,
            max_length=max_length,
        )
    ).parsed
