from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResearchPaperMetadataItem")


@_attrs_define
class ResearchPaperMetadataItem:
    """Metadata for a research paper.

    Attributes:
        title (None | str | Unset): Paper title
        authors (list[str] | None | Unset): List of author names
        abstract (None | str | Unset): Paper abstract
        categories (list[str] | None | Unset): arXiv categories
        primary_category (None | str | Unset): Primary arXiv category
        published_date (None | str | Unset): Publication date
        doi (None | str | Unset): Digital Object Identifier
        pdf_url (None | str | Unset): URL to PDF
        abs_url (None | str | Unset): URL to abstract page
    """

    title: None | str | Unset = UNSET
    authors: list[str] | None | Unset = UNSET
    abstract: None | str | Unset = UNSET
    categories: list[str] | None | Unset = UNSET
    primary_category: None | str | Unset = UNSET
    published_date: None | str | Unset = UNSET
    doi: None | str | Unset = UNSET
    pdf_url: None | str | Unset = UNSET
    abs_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        authors: list[str] | None | Unset
        if isinstance(self.authors, Unset):
            authors = UNSET
        elif isinstance(self.authors, list):
            authors = self.authors

        else:
            authors = self.authors

        abstract: None | str | Unset
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        else:
            abstract = self.abstract

        categories: list[str] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories

        else:
            categories = self.categories

        primary_category: None | str | Unset
        if isinstance(self.primary_category, Unset):
            primary_category = UNSET
        else:
            primary_category = self.primary_category

        published_date: None | str | Unset
        if isinstance(self.published_date, Unset):
            published_date = UNSET
        else:
            published_date = self.published_date

        doi: None | str | Unset
        if isinstance(self.doi, Unset):
            doi = UNSET
        else:
            doi = self.doi

        pdf_url: None | str | Unset
        if isinstance(self.pdf_url, Unset):
            pdf_url = UNSET
        else:
            pdf_url = self.pdf_url

        abs_url: None | str | Unset
        if isinstance(self.abs_url, Unset):
            abs_url = UNSET
        else:
            abs_url = self.abs_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if authors is not UNSET:
            field_dict["authors"] = authors
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if categories is not UNSET:
            field_dict["categories"] = categories
        if primary_category is not UNSET:
            field_dict["primary_category"] = primary_category
        if published_date is not UNSET:
            field_dict["published_date"] = published_date
        if doi is not UNSET:
            field_dict["doi"] = doi
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if abs_url is not UNSET:
            field_dict["abs_url"] = abs_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        def _parse_abstract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abstract = _parse_abstract(d.pop("abstract", UNSET))

        def _parse_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[str], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_primary_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_category = _parse_primary_category(d.pop("primary_category", UNSET))

        def _parse_published_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_date = _parse_published_date(d.pop("published_date", UNSET))

        def _parse_doi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        doi = _parse_doi(d.pop("doi", UNSET))

        def _parse_pdf_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_url = _parse_pdf_url(d.pop("pdf_url", UNSET))

        def _parse_abs_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abs_url = _parse_abs_url(d.pop("abs_url", UNSET))

        research_paper_metadata_item = cls(
            title=title,
            authors=authors,
            abstract=abstract,
            categories=categories,
            primary_category=primary_category,
            published_date=published_date,
            doi=doi,
            pdf_url=pdf_url,
            abs_url=abs_url,
        )

        research_paper_metadata_item.additional_properties = d
        return research_paper_metadata_item

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
