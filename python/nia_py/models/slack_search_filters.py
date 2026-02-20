from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackSearchFilters")


@_attrs_define
class SlackSearchFilters:
    """Filters for Slack message search within query endpoint.

    Attributes:
        channels (list[str] | None | Unset): Filter by channel names or IDs
        users (list[str] | None | Unset): Filter by Slack user names or IDs
        date_from (None | str | Unset): Oldest message timestamp (ISO 8601)
        date_to (None | str | Unset): Newest message timestamp (ISO 8601)
        include_threads (bool | Unset): Include threaded messages in results Default: True.
    """

    channels: list[str] | None | Unset = UNSET
    users: list[str] | None | Unset = UNSET
    date_from: None | str | Unset = UNSET
    date_to: None | str | Unset = UNSET
    include_threads: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: list[str] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = self.channels

        else:
            channels = self.channels

        users: list[str] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = self.users

        else:
            users = self.users

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        else:
            date_to = self.date_to

        include_threads = self.include_threads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if users is not UNSET:
            field_dict["users"] = users
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if include_threads is not UNSET:
            field_dict["include_threads"] = include_threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = cast(list[str], data)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))

        def _parse_users(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = cast(list[str], data)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        def _parse_date_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        include_threads = d.pop("include_threads", UNSET)

        slack_search_filters = cls(
            channels=channels,
            users=users,
            date_from=date_from,
            date_to=date_to,
            include_threads=include_threads,
        )

        slack_search_filters.additional_properties = d
        return slack_search_filters

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
