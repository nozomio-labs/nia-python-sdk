from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackChannelsConfigRequest")


@_attrs_define
class SlackChannelsConfigRequest:
    """Configure which channels to index.

    Attributes:
        mode (str | Unset): 'all' to index all channels, 'selected' to pick specific ones Default: 'all'.
        include_channels (list[str] | None | Unset): Channel IDs to include (when mode='selected')
        exclude_channels (list[str] | None | Unset): Channel IDs to exclude
    """

    mode: str | Unset = "all"
    include_channels: list[str] | None | Unset = UNSET
    exclude_channels: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        include_channels: list[str] | None | Unset
        if isinstance(self.include_channels, Unset):
            include_channels = UNSET
        elif isinstance(self.include_channels, list):
            include_channels = self.include_channels

        else:
            include_channels = self.include_channels

        exclude_channels: list[str] | None | Unset
        if isinstance(self.exclude_channels, Unset):
            exclude_channels = UNSET
        elif isinstance(self.exclude_channels, list):
            exclude_channels = self.exclude_channels

        else:
            exclude_channels = self.exclude_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if include_channels is not UNSET:
            field_dict["include_channels"] = include_channels
        if exclude_channels is not UNSET:
            field_dict["exclude_channels"] = exclude_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = d.pop("mode", UNSET)

        def _parse_include_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_channels_type_0 = cast(list[str], data)

                return include_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_channels = _parse_include_channels(d.pop("include_channels", UNSET))

        def _parse_exclude_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_channels_type_0 = cast(list[str], data)

                return exclude_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_channels = _parse_exclude_channels(d.pop("exclude_channels", UNSET))

        slack_channels_config_request = cls(
            mode=mode,
            include_channels=include_channels,
            exclude_channels=exclude_channels,
        )

        slack_channels_config_request.additional_properties = d
        return slack_channels_config_request

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
