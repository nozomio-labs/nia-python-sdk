from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_info import PaginationInfo
    from ..models.source import Source


T = TypeVar("T", bound="SourceListResponse")


@_attrs_define
class SourceListResponse:
    """Response for listing sources.

    Attributes:
        pagination (PaginationInfo): Pagination metadata.
        items (list[Source] | Unset): List of sources
    """

    pagination: PaginationInfo
    items: list[Source] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_info import PaginationInfo
        from ..models.source import Source

        d = dict(src_dict)
        pagination = PaginationInfo.from_dict(d.pop("pagination"))

        _items = d.pop("items", UNSET)
        items: list[Source] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = Source.from_dict(items_item_data)

                items.append(items_item)

        source_list_response = cls(
            pagination=pagination,
            items=items,
        )

        source_list_response.additional_properties = d
        return source_list_response

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
