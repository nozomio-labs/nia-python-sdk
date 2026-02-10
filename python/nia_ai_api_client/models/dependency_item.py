from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DependencyItem")


@_attrs_define
class DependencyItem:
    """
    Attributes:
        name (str):
        version (None | str):
        registry (str):
        is_dev (bool):
    """

    name: str
    version: None | str
    registry: str
    is_dev: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version: None | str
        version = self.version

        registry = self.registry

        is_dev = self.is_dev

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "registry": registry,
                "is_dev": is_dev,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        registry = d.pop("registry")

        is_dev = d.pop("is_dev")

        dependency_item = cls(
            name=name,
            version=version,
            registry=registry,
            is_dev=is_dev,
        )

        dependency_item.additional_properties = d
        return dependency_item

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
