from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubGlobRequest")


@_attrs_define
class GitHubGlobRequest:
    """
    Attributes:
        repository (str): Repository in owner/repo format
        pattern (str): Glob pattern (e.g., '*.py', 'src/**/*.ts')
        ref (str | Unset): Branch, tag, or commit SHA Default: 'HEAD'.
    """

    repository: str
    pattern: str
    ref: str | Unset = "HEAD"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        pattern = self.pattern

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "pattern": pattern,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository = d.pop("repository")

        pattern = d.pop("pattern")

        ref = d.pop("ref", UNSET)

        git_hub_glob_request = cls(
            repository=repository,
            pattern=pattern,
            ref=ref,
        )

        git_hub_glob_request.additional_properties = d
        return git_hub_glob_request

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
