from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_and_subscribe_v2_dependencies_upload_post import (
    BodyUploadAndSubscribeV2DependenciesUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.subscribe_response import SubscribeResponse
from ...types import Response


def _get_kwargs(
    *,
    body: BodyUploadAndSubscribeV2DependenciesUploadPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dependencies/upload",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SubscribeResponse | None:
    if response.status_code == 200:
        response_200 = SubscribeResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SubscribeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadAndSubscribeV2DependenciesUploadPost,
) -> Response[HTTPValidationError | SubscribeResponse]:
    """Upload manifest file and subscribe to dependencies

     Upload a package manifest file and subscribe to documentation for all dependencies.

    Args:
        body (BodyUploadAndSubscribeV2DependenciesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubscribeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadAndSubscribeV2DependenciesUploadPost,
) -> HTTPValidationError | SubscribeResponse | None:
    """Upload manifest file and subscribe to dependencies

     Upload a package manifest file and subscribe to documentation for all dependencies.

    Args:
        body (BodyUploadAndSubscribeV2DependenciesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubscribeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadAndSubscribeV2DependenciesUploadPost,
) -> Response[HTTPValidationError | SubscribeResponse]:
    """Upload manifest file and subscribe to dependencies

     Upload a package manifest file and subscribe to documentation for all dependencies.

    Args:
        body (BodyUploadAndSubscribeV2DependenciesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubscribeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadAndSubscribeV2DependenciesUploadPost,
) -> HTTPValidationError | SubscribeResponse | None:
    """Upload manifest file and subscribe to dependencies

     Upload a package manifest file and subscribe to documentation for all dependencies.

    Args:
        body (BodyUploadAndSubscribeV2DependenciesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubscribeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
