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
    channel: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_channel: None | str | Unset
    if isinstance(channel, Unset):
        json_channel = UNSET
    else:
        json_channel = channel
    params["channel"] = json_channel

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slack/installations/{installation_id}/messages".format(
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
    channel: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[Any | HTTPValidationError]:
    """Read Slack Messages

     Read recent messages from a Slack channel (live from Slack API).

    Args:
        installation_id (str):
        channel (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        installation_id=installation_id,
        channel=channel,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    channel: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Any | HTTPValidationError | None:
    """Read Slack Messages

     Read recent messages from a Slack channel (live from Slack API).

    Args:
        installation_id (str):
        channel (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        installation_id=installation_id,
        client=client,
        channel=channel,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    channel: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[Any | HTTPValidationError]:
    """Read Slack Messages

     Read recent messages from a Slack channel (live from Slack API).

    Args:
        installation_id (str):
        channel (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        installation_id=installation_id,
        channel=channel,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    installation_id: str,
    *,
    client: AuthenticatedClient | Client,
    channel: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Any | HTTPValidationError | None:
    """Read Slack Messages

     Read recent messages from a Slack channel (live from Slack API).

    Args:
        installation_id (str):
        channel (None | str | Unset):
        limit (int | Unset):  Default: 50.

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
            channel=channel,
            limit=limit,
        )
    ).parsed
