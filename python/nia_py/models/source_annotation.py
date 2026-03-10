from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_annotation_kind import SourceAnnotationKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceAnnotation")


@_attrs_define
class SourceAnnotation:
    """A saved note attached to a source.

    Attributes:
        id (str): Annotation identifier
        content (str): Annotation text
        kind (SourceAnnotationKind | Unset): Annotation category Default: SourceAnnotationKind.NOTE.
        created_at (None | str | Unset): Creation timestamp (ISO)
        updated_at (None | str | Unset): Last update timestamp (ISO)
    """

    id: str
    content: str
    kind: SourceAnnotationKind | Unset = SourceAnnotationKind.NOTE
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content = self.content

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "content": content,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        content = d.pop("content")

        _kind = d.pop("kind", UNSET)
        kind: SourceAnnotationKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = SourceAnnotationKind(_kind)

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        source_annotation = cls(
            id=id,
            content=content,
            kind=kind,
            created_at=created_at,
            updated_at=updated_at,
        )

        source_annotation.additional_properties = d
        return source_annotation

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
