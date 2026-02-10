from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_tree_stats_file_extensions import RepositoryTreeStatsFileExtensions


T = TypeVar("T", bound="RepositoryTreeStats")


@_attrs_define
class RepositoryTreeStats:
    """Statistics about a repository tree.

    Attributes:
        total_files (int | Unset): Total number of files Default: 0.
        total_directories (int | Unset): Total number of directories Default: 0.
        total_items (int | Unset): Total number of items Default: 0.
        file_extensions (RepositoryTreeStatsFileExtensions | Unset): File extension counts
        max_depth (int | Unset): Maximum tree depth Default: 0.
    """

    total_files: int | Unset = 0
    total_directories: int | Unset = 0
    total_items: int | Unset = 0
    file_extensions: RepositoryTreeStatsFileExtensions | Unset = UNSET
    max_depth: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_files = self.total_files

        total_directories = self.total_directories

        total_items = self.total_items

        file_extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_extensions, Unset):
            file_extensions = self.file_extensions.to_dict()

        max_depth = self.max_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_files is not UNSET:
            field_dict["total_files"] = total_files
        if total_directories is not UNSET:
            field_dict["total_directories"] = total_directories
        if total_items is not UNSET:
            field_dict["total_items"] = total_items
        if file_extensions is not UNSET:
            field_dict["file_extensions"] = file_extensions
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_tree_stats_file_extensions import RepositoryTreeStatsFileExtensions

        d = dict(src_dict)
        total_files = d.pop("total_files", UNSET)

        total_directories = d.pop("total_directories", UNSET)

        total_items = d.pop("total_items", UNSET)

        _file_extensions = d.pop("file_extensions", UNSET)
        file_extensions: RepositoryTreeStatsFileExtensions | Unset
        if isinstance(_file_extensions, Unset):
            file_extensions = UNSET
        else:
            file_extensions = RepositoryTreeStatsFileExtensions.from_dict(_file_extensions)

        max_depth = d.pop("max_depth", UNSET)

        repository_tree_stats = cls(
            total_files=total_files,
            total_directories=total_directories,
            total_items=total_items,
            file_extensions=file_extensions,
            max_depth=max_depth,
        )

        repository_tree_stats.additional_properties = d
        return repository_tree_stats

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
