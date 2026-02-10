from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_grep_match_detail import DocGrepMatchDetail


T = TypeVar("T", bound="DocGrepFileMatch")


@_attrs_define
class DocGrepFileMatch:
    """Grep matches grouped by file.

    Attributes:
        path (str): Virtual path
        url (None | str | Unset): Original URL
        matches (list[DocGrepMatchDetail] | Unset): Matches in this file
    """

    path: str
    url: None | str | Unset = UNSET
    matches: list[DocGrepMatchDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        matches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.doc_grep_match_detail import DocGrepMatchDetail

        d = dict(src_dict)
        path = d.pop("path")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        _matches = d.pop("matches", UNSET)
        matches: list[DocGrepMatchDetail] | Unset = UNSET
        if _matches is not UNSET:
            matches = []
            for matches_item_data in _matches:
                matches_item = DocGrepMatchDetail.from_dict(matches_item_data)

                matches.append(matches_item)

        doc_grep_file_match = cls(
            path=path,
            url=url,
            matches=matches,
        )

        doc_grep_file_match.additional_properties = d
        return doc_grep_file_match

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
