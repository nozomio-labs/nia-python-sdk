from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClassifyLocalFolderRequest")


@_attrs_define
class ClassifyLocalFolderRequest:
    """Request to classify local folder content.

    Attributes:
        categories (list[str]): Categories to classify content into (2-10 categories)
        include_uncategorized (bool | Unset): Whether to include an 'Uncategorized' bucket for edge cases Default: True.
    """

    categories: list[str]
    include_uncategorized: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories

        include_uncategorized = self.include_uncategorized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
            }
        )
        if include_uncategorized is not UNSET:
            field_dict["include_uncategorized"] = include_uncategorized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = cast(list[str], d.pop("categories"))

        include_uncategorized = d.pop("include_uncategorized", UNSET)

        classify_local_folder_request = cls(
            categories=categories,
            include_uncategorized=include_uncategorized,
        )

        classify_local_folder_request.additional_properties = d
        return classify_local_folder_request

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
