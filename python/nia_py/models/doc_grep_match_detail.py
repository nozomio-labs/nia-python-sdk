from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocGrepMatchDetail")


@_attrs_define
class DocGrepMatchDetail:
    """A single line match within a documentation file.

    Attributes:
        line (str): The matching line content
        context_start_line (int): Starting line number of context
        context (list[str] | Unset): Context lines around the match
        line_number (int | None | Unset): Line number of the match
    """

    line: str
    context_start_line: int
    context: list[str] | Unset = UNSET
    line_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line = self.line

        context_start_line = self.context_start_line

        context: list[str] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context

        line_number: int | None | Unset
        if isinstance(self.line_number, Unset):
            line_number = UNSET
        else:
            line_number = self.line_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line": line,
                "context_start_line": context_start_line,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if line_number is not UNSET:
            field_dict["line_number"] = line_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line = d.pop("line")

        context_start_line = d.pop("context_start_line")

        context = cast(list[str], d.pop("context", UNSET))

        def _parse_line_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line_number = _parse_line_number(d.pop("line_number", UNSET))

        doc_grep_match_detail = cls(
            line=line,
            context_start_line=context_start_line,
            context=context,
            line_number=line_number,
        )

        doc_grep_match_detail.additional_properties = d
        return doc_grep_match_detail

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
