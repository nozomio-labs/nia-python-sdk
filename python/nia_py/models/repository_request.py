from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryRequest")


@_attrs_define
class RepositoryRequest:
    """
    Attributes:
        repository (str): Repository identifier in owner/repo format
        branch (None | str | Unset): Branch to index, defaults to repository's default branch
        ref (None | str | Unset): Git ref to index (branch, tag, or commit SHA). Takes precedence over branch.
        add_as_global_source (bool | Unset): Add to global shared pool (default: True). Set False for private indexing
            of public repos. Default: True.
    """

    repository: str
    branch: None | str | Unset = UNSET
    ref: None | str | Unset = UNSET
    add_as_global_source: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        add_as_global_source = self.add_as_global_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if ref is not UNSET:
            field_dict["ref"] = ref
        if add_as_global_source is not UNSET:
            field_dict["add_as_global_source"] = add_as_global_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository = d.pop("repository")

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("ref", UNSET))

        add_as_global_source = d.pop("add_as_global_source", UNSET)

        repository_request = cls(
            repository=repository,
            branch=branch,
            ref=ref,
            add_as_global_source=add_as_global_source,
        )

        repository_request.additional_properties = d
        return repository_request

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
