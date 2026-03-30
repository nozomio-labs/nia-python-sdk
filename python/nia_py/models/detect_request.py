from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetectRequest")


@_attrs_define
class DetectRequest:
    """
    Attributes:
        url (None | str | Unset):
        source_id (None | str | Unset):
        page_range (None | str | Unset):
        include_symbols (bool | Unset):  Default: False.
        filter_pattern (None | str | Unset):
    """

    url: None | str | Unset = UNSET
    source_id: None | str | Unset = UNSET
    page_range: None | str | Unset = UNSET
    include_symbols: bool | Unset = False
    filter_pattern: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        page_range: None | str | Unset
        if isinstance(self.page_range, Unset):
            page_range = UNSET
        else:
            page_range = self.page_range

        include_symbols = self.include_symbols

        filter_pattern: None | str | Unset
        if isinstance(self.filter_pattern, Unset):
            filter_pattern = UNSET
        else:
            filter_pattern = self.filter_pattern

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if page_range is not UNSET:
            field_dict["page_range"] = page_range
        if include_symbols is not UNSET:
            field_dict["include_symbols"] = include_symbols
        if filter_pattern is not UNSET:
            field_dict["filter_pattern"] = filter_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_page_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_range = _parse_page_range(d.pop("page_range", UNSET))

        include_symbols = d.pop("include_symbols", UNSET)

        def _parse_filter_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_pattern = _parse_filter_pattern(d.pop("filter_pattern", UNSET))

        detect_request = cls(
            url=url,
            source_id=source_id,
            page_range=page_range,
            include_symbols=include_symbols,
            filter_pattern=filter_pattern,
        )

        detect_request.additional_properties = d
        return detect_request

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
