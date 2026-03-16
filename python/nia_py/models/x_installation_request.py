from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XInstallationRequest")


@_attrs_define
class XInstallationRequest:
    """
    Attributes:
        username (str): X username to index (with or without @)
        bearer_token (str): X API bearer token
        display_name (None | str | Unset): Optional custom display name for this source
        max_results (int | Unset): Maximum number of recent posts to index Default: 100.
        include_replies (bool | Unset): Whether replies should be indexed Default: False.
        include_retweets (bool | Unset): Whether reposts/retweets should be indexed Default: False.
    """

    username: str
    bearer_token: str
    display_name: None | str | Unset = UNSET
    max_results: int | Unset = 100
    include_replies: bool | Unset = False
    include_retweets: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        bearer_token = self.bearer_token

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        max_results = self.max_results

        include_replies = self.include_replies

        include_retweets = self.include_retweets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "bearer_token": bearer_token,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if max_results is not UNSET:
            field_dict["max_results"] = max_results
        if include_replies is not UNSET:
            field_dict["include_replies"] = include_replies
        if include_retweets is not UNSET:
            field_dict["include_retweets"] = include_retweets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        bearer_token = d.pop("bearer_token")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        max_results = d.pop("max_results", UNSET)

        include_replies = d.pop("include_replies", UNSET)

        include_retweets = d.pop("include_retweets", UNSET)

        x_installation_request = cls(
            username=username,
            bearer_token=bearer_token,
            display_name=display_name,
            max_results=max_results,
            include_replies=include_replies,
            include_retweets=include_retweets,
        )

        x_installation_request.additional_properties = d
        return x_installation_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
