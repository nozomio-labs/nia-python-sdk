from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_request_manifest import ImportRequestManifest


T = TypeVar("T", bound="ImportRequest")


@_attrs_define
class ImportRequest:
    """
    Attributes:
        manifest (ImportRequestManifest): The export manifest JSON
        skip_private_repos (bool | Unset):  Default: False.
        skip_contexts (bool | Unset):  Default: False.
    """

    manifest: ImportRequestManifest
    skip_private_repos: bool | Unset = False
    skip_contexts: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest = self.manifest.to_dict()

        skip_private_repos = self.skip_private_repos

        skip_contexts = self.skip_contexts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manifest": manifest,
            }
        )
        if skip_private_repos is not UNSET:
            field_dict["skip_private_repos"] = skip_private_repos
        if skip_contexts is not UNSET:
            field_dict["skip_contexts"] = skip_contexts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_request_manifest import ImportRequestManifest

        d = dict(src_dict)
        manifest = ImportRequestManifest.from_dict(d.pop("manifest"))

        skip_private_repos = d.pop("skip_private_repos", UNSET)

        skip_contexts = d.pop("skip_contexts", UNSET)

        import_request = cls(
            manifest=manifest,
            skip_private_repos=skip_private_repos,
            skip_contexts=skip_contexts,
        )

        import_request.additional_properties = d
        return import_request

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
