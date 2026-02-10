from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dependency_subscribe_request_manifest_type_type_0 import DependencySubscribeRequestManifestTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="DependencySubscribeRequest")


@_attrs_define
class DependencySubscribeRequest:
    """
    Attributes:
        manifest_content (str): Raw content of the manifest file
        manifest_type (DependencySubscribeRequestManifestTypeType0 | None | Unset): Manifest type. Auto-detected if not
            provided.
        filename (None | str | Unset): Original filename for type detection
        include_dev_dependencies (bool | Unset): Include devDependencies/dev-dependencies Default: False.
        max_new_indexes (int | Unset): Max number of new indexes to start (0-500) Default: 150.
    """

    manifest_content: str
    manifest_type: DependencySubscribeRequestManifestTypeType0 | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    include_dev_dependencies: bool | Unset = False
    max_new_indexes: int | Unset = 150
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest_content = self.manifest_content

        manifest_type: None | str | Unset
        if isinstance(self.manifest_type, Unset):
            manifest_type = UNSET
        elif isinstance(self.manifest_type, DependencySubscribeRequestManifestTypeType0):
            manifest_type = self.manifest_type.value
        else:
            manifest_type = self.manifest_type

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        include_dev_dependencies = self.include_dev_dependencies

        max_new_indexes = self.max_new_indexes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manifest_content": manifest_content,
            }
        )
        if manifest_type is not UNSET:
            field_dict["manifest_type"] = manifest_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if include_dev_dependencies is not UNSET:
            field_dict["include_dev_dependencies"] = include_dev_dependencies
        if max_new_indexes is not UNSET:
            field_dict["max_new_indexes"] = max_new_indexes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manifest_content = d.pop("manifest_content")

        def _parse_manifest_type(data: object) -> DependencySubscribeRequestManifestTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manifest_type_type_0 = DependencySubscribeRequestManifestTypeType0(data)

                return manifest_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DependencySubscribeRequestManifestTypeType0 | None | Unset, data)

        manifest_type = _parse_manifest_type(d.pop("manifest_type", UNSET))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        include_dev_dependencies = d.pop("include_dev_dependencies", UNSET)

        max_new_indexes = d.pop("max_new_indexes", UNSET)

        dependency_subscribe_request = cls(
            manifest_content=manifest_content,
            manifest_type=manifest_type,
            filename=filename,
            include_dev_dependencies=include_dev_dependencies,
            max_new_indexes=max_new_indexes,
        )

        dependency_subscribe_request.additional_properties = d
        return dependency_subscribe_request

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
