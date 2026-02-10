from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MappingItem")


@_attrs_define
class MappingItem:
    """
    Attributes:
        name (str):
        registry (str):
        docs_url (None | str):
        mapping_source (str):
        confidence (float):
    """

    name: str
    registry: str
    docs_url: None | str
    mapping_source: str
    confidence: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        registry = self.registry

        docs_url: None | str
        docs_url = self.docs_url

        mapping_source = self.mapping_source

        confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "registry": registry,
                "docs_url": docs_url,
                "mapping_source": mapping_source,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        registry = d.pop("registry")

        def _parse_docs_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        docs_url = _parse_docs_url(d.pop("docs_url"))

        mapping_source = d.pop("mapping_source")

        confidence = d.pop("confidence")

        mapping_item = cls(
            name=name,
            registry=registry,
            docs_url=docs_url,
            mapping_source=mapping_source,
            confidence=confidence,
        )

        mapping_item.additional_properties = d
        return mapping_item

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
