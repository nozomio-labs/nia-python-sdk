from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.research_paper_metadata_item import ResearchPaperMetadataItem


T = TypeVar("T", bound="ResearchPaperItem")


@_attrs_define
class ResearchPaperItem:
    """A single research paper.

    Attributes:
        id (str): Paper ID
        status (str): Indexing status
        title (None | str | Unset): Paper title
        arxiv_id (None | str | Unset): arXiv ID
        url (None | str | Unset): Paper URL
        source_type (str | Unset): Source type Default: 'research_paper'.
        is_active (bool | Unset): Whether paper is active Default: True.
        created_at (datetime.datetime | None | Unset): When indexed
        updated_at (datetime.datetime | None | Unset): Last updated
        page_count (int | None | Unset): Number of pages
        chunk_count (int | None | Unset): Number of chunks
        display_name (None | str | Unset): Display name
        metadata (None | ResearchPaperMetadataItem | Unset): Paper metadata
        authors (list[str] | None | Unset): Paper authors
        error (None | str | Unset): Error message if failed
    """

    id: str
    status: str
    title: None | str | Unset = UNSET
    arxiv_id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    source_type: str | Unset = "research_paper"
    is_active: bool | Unset = True
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    page_count: int | None | Unset = UNSET
    chunk_count: int | None | Unset = UNSET
    display_name: None | str | Unset = UNSET
    metadata: None | ResearchPaperMetadataItem | Unset = UNSET
    authors: list[str] | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.research_paper_metadata_item import ResearchPaperMetadataItem

        id = self.id

        status = self.status

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        arxiv_id: None | str | Unset
        if isinstance(self.arxiv_id, Unset):
            arxiv_id = UNSET
        else:
            arxiv_id = self.arxiv_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source_type = self.source_type

        is_active = self.is_active

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        page_count: int | None | Unset
        if isinstance(self.page_count, Unset):
            page_count = UNSET
        else:
            page_count = self.page_count

        chunk_count: int | None | Unset
        if isinstance(self.chunk_count, Unset):
            chunk_count = UNSET
        else:
            chunk_count = self.chunk_count

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ResearchPaperMetadataItem):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        authors: list[str] | None | Unset
        if isinstance(self.authors, Unset):
            authors = UNSET
        elif isinstance(self.authors, list):
            authors = self.authors

        else:
            authors = self.authors

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if arxiv_id is not UNSET:
            field_dict["arxiv_id"] = arxiv_id
        if url is not UNSET:
            field_dict["url"] = url
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if chunk_count is not UNSET:
            field_dict["chunk_count"] = chunk_count
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if authors is not UNSET:
            field_dict["authors"] = authors
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.research_paper_metadata_item import ResearchPaperMetadataItem

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_arxiv_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        arxiv_id = _parse_arxiv_id(d.pop("arxiv_id", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        source_type = d.pop("source_type", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_page_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_count = _parse_page_count(d.pop("page_count", UNSET))

        def _parse_chunk_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_count = _parse_chunk_count(d.pop("chunk_count", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_metadata(data: object) -> None | ResearchPaperMetadataItem | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ResearchPaperMetadataItem.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResearchPaperMetadataItem | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_authors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = cast(list[str], data)

                return authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        authors = _parse_authors(d.pop("authors", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        research_paper_item = cls(
            id=id,
            status=status,
            title=title,
            arxiv_id=arxiv_id,
            url=url,
            source_type=source_type,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            page_count=page_count,
            chunk_count=chunk_count,
            display_name=display_name,
            metadata=metadata,
            authors=authors,
            error=error,
        )

        research_paper_item.additional_properties = d
        return research_paper_item

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
