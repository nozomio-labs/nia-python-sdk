from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchScope")


@_attrs_define
class SearchScope:
    """Scope for searching Nia's indexed sources.

    Attributes:
        repositories (list[str] | None | Unset): Repository identifiers to search
        data_sources (list[str] | None | Unset): Documentation source IDs to search
    """

    repositories: list[str] | None | Unset = UNSET
    data_sources: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repositories: list[str] | None | Unset
        if isinstance(self.repositories, Unset):
            repositories = UNSET
        elif isinstance(self.repositories, list):
            repositories = self.repositories

        else:
            repositories = self.repositories

        data_sources: list[str] | None | Unset
        if isinstance(self.data_sources, Unset):
            data_sources = UNSET
        elif isinstance(self.data_sources, list):
            data_sources = self.data_sources

        else:
            data_sources = self.data_sources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if data_sources is not UNSET:
            field_dict["data_sources"] = data_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_repositories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repositories_type_0 = cast(list[str], data)

                return repositories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        repositories = _parse_repositories(d.pop("repositories", UNSET))

        def _parse_data_sources(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_sources_type_0 = cast(list[str], data)

                return data_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        data_sources = _parse_data_sources(d.pop("data_sources", UNSET))

        search_scope = cls(
            repositories=repositories,
            data_sources=data_sources,
        )

        search_scope.additional_properties = d
        return search_scope

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
