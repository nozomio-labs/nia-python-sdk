from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubSearchRequest")


@_attrs_define
class GitHubSearchRequest:
    """
    Attributes:
        query (str): Code search query
        repository (str): Repository in owner/repo format
        per_page (int | Unset): Results per page Default: 30.
        page (int | Unset): Page number Default: 1.
    """

    query: str
    repository: str
    per_page: int | Unset = 30
    page: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        repository = self.repository

        per_page = self.per_page

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "repository": repository,
            }
        )
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        repository = d.pop("repository")

        per_page = d.pop("per_page", UNSET)

        page = d.pop("page", UNSET)

        git_hub_search_request = cls(
            query=query,
            repository=repository,
            per_page=per_page,
            page=page,
        )

        git_hub_search_request.additional_properties = d
        return git_hub_search_request

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
