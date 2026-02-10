from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResearchPaperRequest")


@_attrs_define
class ResearchPaperRequest:
    """Request model for indexing a research paper (arXiv).

    Attributes:
        url (str): arXiv URL or raw ID (e.g., '2312.00752', 'https://arxiv.org/abs/2312.00752')
        organization_id (None | str | Unset): Organization ID for team-level indexing
        add_as_global_source (bool | Unset): Add to global shared pool (default: True). Set False for private indexing.
            Default: True.
    """

    url: str
    organization_id: None | str | Unset = UNSET
    add_as_global_source: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        add_as_global_source = self.add_as_global_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if add_as_global_source is not UNSET:
            field_dict["add_as_global_source"] = add_as_global_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        add_as_global_source = d.pop("add_as_global_source", UNSET)

        research_paper_request = cls(
            url=url,
            organization_id=organization_id,
            add_as_global_source=add_as_global_source,
        )

        research_paper_request.additional_properties = d
        return research_paper_request

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
