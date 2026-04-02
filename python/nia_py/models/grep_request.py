from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrepRequest")


@_attrs_define
class GrepRequest:
    """
    Attributes:
        pattern (str): Regex pattern
        path (str | Unset): Path prefix filter Default: ''.
        case_sensitive (bool | Unset):  Default: False.
        whole_word (bool | Unset):  Default: False.
        fixed_string (bool | Unset):  Default: False.
        max_total_matches (int | Unset):  Default: 100.
        max_matches_per_file (int | Unset):  Default: 10.
        context_lines (int | Unset):  Default: 3.
        lines_before (int | None | Unset):
        lines_after (int | None | Unset):
        output_mode (str | Unset): content|files_with_matches|count Default: 'content'.
        multiline_content (bool | Unset):  Default: False.
    """

    pattern: str
    path: str | Unset = ""
    case_sensitive: bool | Unset = False
    whole_word: bool | Unset = False
    fixed_string: bool | Unset = False
    max_total_matches: int | Unset = 100
    max_matches_per_file: int | Unset = 10
    context_lines: int | Unset = 3
    lines_before: int | None | Unset = UNSET
    lines_after: int | None | Unset = UNSET
    output_mode: str | Unset = "content"
    multiline_content: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        path = self.path

        case_sensitive = self.case_sensitive

        whole_word = self.whole_word

        fixed_string = self.fixed_string

        max_total_matches = self.max_total_matches

        max_matches_per_file = self.max_matches_per_file

        context_lines = self.context_lines

        lines_before: int | None | Unset
        if isinstance(self.lines_before, Unset):
            lines_before = UNSET
        else:
            lines_before = self.lines_before

        lines_after: int | None | Unset
        if isinstance(self.lines_after, Unset):
            lines_after = UNSET
        else:
            lines_after = self.lines_after

        output_mode = self.output_mode

        multiline_content = self.multiline_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive
        if whole_word is not UNSET:
            field_dict["whole_word"] = whole_word
        if fixed_string is not UNSET:
            field_dict["fixed_string"] = fixed_string
        if max_total_matches is not UNSET:
            field_dict["max_total_matches"] = max_total_matches
        if max_matches_per_file is not UNSET:
            field_dict["max_matches_per_file"] = max_matches_per_file
        if context_lines is not UNSET:
            field_dict["context_lines"] = context_lines
        if lines_before is not UNSET:
            field_dict["lines_before"] = lines_before
        if lines_after is not UNSET:
            field_dict["lines_after"] = lines_after
        if output_mode is not UNSET:
            field_dict["output_mode"] = output_mode
        if multiline_content is not UNSET:
            field_dict["multiline_content"] = multiline_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pattern = d.pop("pattern")

        path = d.pop("path", UNSET)

        case_sensitive = d.pop("case_sensitive", UNSET)

        whole_word = d.pop("whole_word", UNSET)

        fixed_string = d.pop("fixed_string", UNSET)

        max_total_matches = d.pop("max_total_matches", UNSET)

        max_matches_per_file = d.pop("max_matches_per_file", UNSET)

        context_lines = d.pop("context_lines", UNSET)

        def _parse_lines_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lines_before = _parse_lines_before(d.pop("lines_before", UNSET))

        def _parse_lines_after(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lines_after = _parse_lines_after(d.pop("lines_after", UNSET))

        output_mode = d.pop("output_mode", UNSET)

        multiline_content = d.pop("multiline_content", UNSET)

        grep_request = cls(
            pattern=pattern,
            path=path,
            case_sensitive=case_sensitive,
            whole_word=whole_word,
            fixed_string=fixed_string,
            max_total_matches=max_total_matches,
            max_matches_per_file=max_matches_per_file,
            context_lines=context_lines,
            lines_before=lines_before,
            lines_after=lines_after,
            output_mode=output_mode,
            multiline_content=multiline_content,
        )

        grep_request.additional_properties = d
        return grep_request

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
