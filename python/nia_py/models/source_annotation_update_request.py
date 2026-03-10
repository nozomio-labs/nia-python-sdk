from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_annotation_update_request_kind_type_0 import SourceAnnotationUpdateRequestKindType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceAnnotationUpdateRequest")


@_attrs_define
class SourceAnnotationUpdateRequest:
    """
    Attributes:
        kind (None | SourceAnnotationUpdateRequestKindType0 | Unset): Updated annotation category
        content (None | str | Unset): Updated annotation body
    """

    kind: None | SourceAnnotationUpdateRequestKindType0 | Unset = UNSET
    content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, SourceAnnotationUpdateRequestKindType0):
            kind = self.kind.value
        else:
            kind = self.kind

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_kind(data: object) -> None | SourceAnnotationUpdateRequestKindType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = SourceAnnotationUpdateRequestKindType0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceAnnotationUpdateRequestKindType0 | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        source_annotation_update_request = cls(
            kind=kind,
            content=content,
        )

        source_annotation_update_request.additional_properties = d
        return source_annotation_update_request

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
