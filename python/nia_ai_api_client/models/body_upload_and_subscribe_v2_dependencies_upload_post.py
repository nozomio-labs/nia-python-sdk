from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadAndSubscribeV2DependenciesUploadPost")


@_attrs_define
class BodyUploadAndSubscribeV2DependenciesUploadPost:
    """
    Attributes:
        file (File): Manifest file to upload
        include_dev_dependencies (bool | Unset): Include dev dependencies Default: False.
        max_new_indexes (int | Unset): Max new indexes to start Default: 150.
    """

    file: File
    include_dev_dependencies: bool | Unset = False
    max_new_indexes: int | Unset = 150
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        include_dev_dependencies = self.include_dev_dependencies

        max_new_indexes = self.max_new_indexes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if include_dev_dependencies is not UNSET:
            field_dict["include_dev_dependencies"] = include_dev_dependencies
        if max_new_indexes is not UNSET:
            field_dict["max_new_indexes"] = max_new_indexes

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.include_dev_dependencies, Unset):
            files.append(
                ("include_dev_dependencies", (None, str(self.include_dev_dependencies).encode(), "text/plain"))
            )

        if not isinstance(self.max_new_indexes, Unset):
            files.append(("max_new_indexes", (None, str(self.max_new_indexes).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        include_dev_dependencies = d.pop("include_dev_dependencies", UNSET)

        max_new_indexes = d.pop("max_new_indexes", UNSET)

        body_upload_and_subscribe_v2_dependencies_upload_post = cls(
            file=file,
            include_dev_dependencies=include_dev_dependencies,
            max_new_indexes=max_new_indexes,
        )

        body_upload_and_subscribe_v2_dependencies_upload_post.additional_properties = d
        return body_upload_and_subscribe_v2_dependencies_upload_post

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
