from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubReadRequest")


@_attrs_define
class GitHubReadRequest:
    """
    Attributes:
        repository (str): Repository in owner/repo format
        path (str): File path within the repository
        ref (str | Unset): Branch, tag, or commit SHA Default: 'HEAD'.
        start_line (int | None | Unset): 1-based start line
        end_line (int | None | Unset): 1-based end line (inclusive)
    """

    repository: str
    path: str
    ref: str | Unset = "HEAD"
    start_line: int | None | Unset = UNSET
    end_line: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        path = self.path

        ref = self.ref

        start_line: int | None | Unset
        if isinstance(self.start_line, Unset):
            start_line = UNSET
        else:
            start_line = self.start_line

        end_line: int | None | Unset
        if isinstance(self.end_line, Unset):
            end_line = UNSET
        else:
            end_line = self.end_line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "path": path,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if end_line is not UNSET:
            field_dict["end_line"] = end_line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository = d.pop("repository")

        path = d.pop("path")

        ref = d.pop("ref", UNSET)

        def _parse_start_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_line = _parse_start_line(d.pop("start_line", UNSET))

        def _parse_end_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end_line = _parse_end_line(d.pop("end_line", UNSET))

        git_hub_read_request = cls(
            repository=repository,
            path=path,
            ref=ref,
            start_line=start_line,
            end_line=end_line,
        )

        git_hub_read_request.additional_properties = d
        return git_hub_read_request

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
