from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentCitation")


@_attrs_define
class DocumentCitation:
    """A citation from the document agent with full location metadata.

    Attributes:
        content (str):
        tool_source (str):
        page_number (int | None | Unset):
        section_id (None | str | Unset):
        section_title (None | str | Unset):
        section_path (list[str] | None | Unset):
        source_id (None | str | Unset):
        source_name (None | str | Unset):
    """

    content: str
    tool_source: str
    page_number: int | None | Unset = UNSET
    section_id: None | str | Unset = UNSET
    section_title: None | str | Unset = UNSET
    section_path: list[str] | None | Unset = UNSET
    source_id: None | str | Unset = UNSET
    source_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        tool_source = self.tool_source

        page_number: int | None | Unset
        if isinstance(self.page_number, Unset):
            page_number = UNSET
        else:
            page_number = self.page_number

        section_id: None | str | Unset
        if isinstance(self.section_id, Unset):
            section_id = UNSET
        else:
            section_id = self.section_id

        section_title: None | str | Unset
        if isinstance(self.section_title, Unset):
            section_title = UNSET
        else:
            section_title = self.section_title

        section_path: list[str] | None | Unset
        if isinstance(self.section_path, Unset):
            section_path = UNSET
        elif isinstance(self.section_path, list):
            section_path = self.section_path

        else:
            section_path = self.section_path

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        source_name: None | str | Unset
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "tool_source": tool_source,
            }
        )
        if page_number is not UNSET:
            field_dict["page_number"] = page_number
        if section_id is not UNSET:
            field_dict["section_id"] = section_id
        if section_title is not UNSET:
            field_dict["section_title"] = section_title
        if section_path is not UNSET:
            field_dict["section_path"] = section_path
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_name is not UNSET:
            field_dict["source_name"] = source_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        tool_source = d.pop("tool_source")

        def _parse_page_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_number = _parse_page_number(d.pop("page_number", UNSET))

        def _parse_section_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_id = _parse_section_id(d.pop("section_id", UNSET))

        def _parse_section_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_title = _parse_section_title(d.pop("section_title", UNSET))

        def _parse_section_path(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                section_path_type_0 = cast(list[str], data)

                return section_path_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        section_path = _parse_section_path(d.pop("section_path", UNSET))

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_name = _parse_source_name(d.pop("source_name", UNSET))

        document_citation = cls(
            content=content,
            tool_source=tool_source,
            page_number=page_number,
            section_id=section_id,
            section_title=section_title,
            section_path=section_path,
            source_id=source_id,
            source_name=source_name,
        )

        document_citation.additional_properties = d
        return document_citation

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
