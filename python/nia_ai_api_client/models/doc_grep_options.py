from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocGrepOptions")


@_attrs_define
class DocGrepOptions:
    """Options used for grep search.

    Attributes:
        case_sensitive (bool | Unset): Case-sensitive matching Default: False.
        whole_word (bool | Unset): Match whole words only Default: False.
        fixed_string (bool | Unset): Treat pattern as literal string Default: False.
        lines_before (int | Unset): Lines of context before match Default: 0.
        lines_after (int | Unset): Lines of context after match Default: 0.
        max_matches_per_file (int | Unset): Maximum matches per file Default: 10.
        max_total_matches (int | Unset): Maximum total matches Default: 100.
        output_mode (str | Unset): Output mode Default: 'content'.
        highlight (bool | Unset): Highlight matches Default: False.
    """

    case_sensitive: bool | Unset = False
    whole_word: bool | Unset = False
    fixed_string: bool | Unset = False
    lines_before: int | Unset = 0
    lines_after: int | Unset = 0
    max_matches_per_file: int | Unset = 10
    max_total_matches: int | Unset = 100
    output_mode: str | Unset = "content"
    highlight: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        case_sensitive = self.case_sensitive

        whole_word = self.whole_word

        fixed_string = self.fixed_string

        lines_before = self.lines_before

        lines_after = self.lines_after

        max_matches_per_file = self.max_matches_per_file

        max_total_matches = self.max_total_matches

        output_mode = self.output_mode

        highlight = self.highlight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive
        if whole_word is not UNSET:
            field_dict["whole_word"] = whole_word
        if fixed_string is not UNSET:
            field_dict["fixed_string"] = fixed_string
        if lines_before is not UNSET:
            field_dict["lines_before"] = lines_before
        if lines_after is not UNSET:
            field_dict["lines_after"] = lines_after
        if max_matches_per_file is not UNSET:
            field_dict["max_matches_per_file"] = max_matches_per_file
        if max_total_matches is not UNSET:
            field_dict["max_total_matches"] = max_total_matches
        if output_mode is not UNSET:
            field_dict["output_mode"] = output_mode
        if highlight is not UNSET:
            field_dict["highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        case_sensitive = d.pop("case_sensitive", UNSET)

        whole_word = d.pop("whole_word", UNSET)

        fixed_string = d.pop("fixed_string", UNSET)

        lines_before = d.pop("lines_before", UNSET)

        lines_after = d.pop("lines_after", UNSET)

        max_matches_per_file = d.pop("max_matches_per_file", UNSET)

        max_total_matches = d.pop("max_total_matches", UNSET)

        output_mode = d.pop("output_mode", UNSET)

        highlight = d.pop("highlight", UNSET)

        doc_grep_options = cls(
            case_sensitive=case_sensitive,
            whole_word=whole_word,
            fixed_string=fixed_string,
            lines_before=lines_before,
            lines_after=lines_after,
            max_matches_per_file=max_matches_per_file,
            max_total_matches=max_total_matches,
            output_mode=output_mode,
            highlight=highlight,
        )

        doc_grep_options.additional_properties = d
        return doc_grep_options

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
