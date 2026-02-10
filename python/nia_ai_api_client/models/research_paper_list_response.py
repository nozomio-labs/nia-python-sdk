from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.research_paper_item import ResearchPaperItem


T = TypeVar("T", bound="ResearchPaperListResponse")


@_attrs_define
class ResearchPaperListResponse:
    """Response for listing research papers.

    Attributes:
        total (int): Total number of papers
        papers (list[ResearchPaperItem] | Unset): List of papers
        limit (int | None | Unset): Limit used
        offset (int | None | Unset): Offset used
    """

    total: int
    papers: list[ResearchPaperItem] | Unset = UNSET
    limit: int | None | Unset = UNSET
    offset: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        papers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.papers, Unset):
            papers = []
            for papers_item_data in self.papers:
                papers_item = papers_item_data.to_dict()
                papers.append(papers_item)

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        offset: int | None | Unset
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
            }
        )
        if papers is not UNSET:
            field_dict["papers"] = papers
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.research_paper_item import ResearchPaperItem

        d = dict(src_dict)
        total = d.pop("total")

        _papers = d.pop("papers", UNSET)
        papers: list[ResearchPaperItem] | Unset = UNSET
        if _papers is not UNSET:
            papers = []
            for papers_item_data in _papers:
                papers_item = ResearchPaperItem.from_dict(papers_item_data)

                papers.append(papers_item)

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        offset = _parse_offset(d.pop("offset", UNSET))

        research_paper_list_response = cls(
            total=total,
            papers=papers,
            limit=limit,
            offset=offset,
        )

        research_paper_list_response.additional_properties = d
        return research_paper_list_response

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
