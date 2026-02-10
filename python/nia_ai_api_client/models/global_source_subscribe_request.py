from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.global_source_subscribe_request_source_type_type_0 import GlobalSourceSubscribeRequestSourceTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalSourceSubscribeRequest")


@_attrs_define
class GlobalSourceSubscribeRequest:
    """Request model for subscribing to a global source

    Attributes:
        url (str): URL of the source (GitHub repo, docs URL, arXiv URL/ID, or HuggingFace dataset URL)
        source_type (GlobalSourceSubscribeRequestSourceTypeType0 | None | Unset): Source type. Auto-detected from URL if
            not provided.
        ref (None | str | Unset): Git ref for repositories (branch, tag, or commit SHA)
    """

    url: str
    source_type: GlobalSourceSubscribeRequestSourceTypeType0 | None | Unset = UNSET
    ref: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        elif isinstance(self.source_type, GlobalSourceSubscribeRequestSourceTypeType0):
            source_type = self.source_type.value
        else:
            source_type = self.source_type

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_source_type(data: object) -> GlobalSourceSubscribeRequestSourceTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_type_0 = GlobalSourceSubscribeRequestSourceTypeType0(data)

                return source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GlobalSourceSubscribeRequestSourceTypeType0 | None | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("ref", UNSET))

        global_source_subscribe_request = cls(
            url=url,
            source_type=source_type,
            ref=ref,
        )

        global_source_subscribe_request.additional_properties = d
        return global_source_subscribe_request

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
