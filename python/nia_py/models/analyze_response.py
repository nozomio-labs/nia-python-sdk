from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dependency_item import DependencyItem
    from ..models.mapping_item import MappingItem


T = TypeVar("T", bound="AnalyzeResponse")


@_attrs_define
class AnalyzeResponse:
    """
    Attributes:
        manifest_type (str):
        total_dependencies (int):
        dependencies (list[DependencyItem]):
        mappings (list[MappingItem]):
        unmapped_count (int):
        unmapped_packages (list[str]):
    """

    manifest_type: str
    total_dependencies: int
    dependencies: list[DependencyItem]
    mappings: list[MappingItem]
    unmapped_count: int
    unmapped_packages: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest_type = self.manifest_type

        total_dependencies = self.total_dependencies

        dependencies = []
        for dependencies_item_data in self.dependencies:
            dependencies_item = dependencies_item_data.to_dict()
            dependencies.append(dependencies_item)

        mappings = []
        for mappings_item_data in self.mappings:
            mappings_item = mappings_item_data.to_dict()
            mappings.append(mappings_item)

        unmapped_count = self.unmapped_count

        unmapped_packages = self.unmapped_packages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manifest_type": manifest_type,
                "total_dependencies": total_dependencies,
                "dependencies": dependencies,
                "mappings": mappings,
                "unmapped_count": unmapped_count,
                "unmapped_packages": unmapped_packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dependency_item import DependencyItem
        from ..models.mapping_item import MappingItem

        d = dict(src_dict)
        manifest_type = d.pop("manifest_type")

        total_dependencies = d.pop("total_dependencies")

        dependencies = []
        _dependencies = d.pop("dependencies")
        for dependencies_item_data in _dependencies:
            dependencies_item = DependencyItem.from_dict(dependencies_item_data)

            dependencies.append(dependencies_item)

        mappings = []
        _mappings = d.pop("mappings")
        for mappings_item_data in _mappings:
            mappings_item = MappingItem.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        unmapped_count = d.pop("unmapped_count")

        unmapped_packages = cast(list[str], d.pop("unmapped_packages"))

        analyze_response = cls(
            manifest_type=manifest_type,
            total_dependencies=total_dependencies,
            dependencies=dependencies,
            mappings=mappings,
            unmapped_count=unmapped_count,
            unmapped_packages=unmapped_packages,
        )

        analyze_response.additional_properties = d
        return analyze_response

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
