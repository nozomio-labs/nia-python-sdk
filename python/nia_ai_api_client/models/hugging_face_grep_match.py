from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HuggingFaceGrepMatch")


@_attrs_define
class HuggingFaceGrepMatch:
    """A single grep match from a HuggingFace dataset (flat format).

    Attributes:
        path (str): Path in format split/row_N
        split (str): Dataset split name
        row_index (int): Row index in the dataset
        line (str | Unset): The matching line content Default: ''.
        context (list[str] | Unset): Context lines around the match
        context_start_line (int | Unset): Starting line number of context Default: 1.
        line_number (int | None | Unset): Line number within the row
    """

    path: str
    split: str
    row_index: int
    line: str | Unset = ""
    context: list[str] | Unset = UNSET
    context_start_line: int | Unset = 1
    line_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        split = self.split

        row_index = self.row_index

        line = self.line

        context: list[str] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context

        context_start_line = self.context_start_line

        line_number: int | None | Unset
        if isinstance(self.line_number, Unset):
            line_number = UNSET
        else:
            line_number = self.line_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "split": split,
                "row_index": row_index,
            }
        )
        if line is not UNSET:
            field_dict["line"] = line
        if context is not UNSET:
            field_dict["context"] = context
        if context_start_line is not UNSET:
            field_dict["context_start_line"] = context_start_line
        if line_number is not UNSET:
            field_dict["line_number"] = line_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        split = d.pop("split")

        row_index = d.pop("row_index")

        line = d.pop("line", UNSET)

        context = cast(list[str], d.pop("context", UNSET))

        context_start_line = d.pop("context_start_line", UNSET)

        def _parse_line_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line_number = _parse_line_number(d.pop("line_number", UNSET))

        hugging_face_grep_match = cls(
            path=path,
            split=split,
            row_index=row_index,
            line=line,
            context=context,
            context_start_line=context_start_line,
            line_number=line_number,
        )

        hugging_face_grep_match.additional_properties = d
        return hugging_face_grep_match

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
