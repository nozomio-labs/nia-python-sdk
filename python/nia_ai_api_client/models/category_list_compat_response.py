from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_list_compat_response_categories_item import CategoryListCompatResponseCategoriesItem
    from ..models.category_list_compat_response_items_item import CategoryListCompatResponseItemsItem
    from ..models.pagination_info import PaginationInfo


T = TypeVar("T", bound="CategoryListCompatResponse")


@_attrs_define
class CategoryListCompatResponse:
    """Backwards-compatible category list response.

    Attributes:
        pagination (PaginationInfo): Pagination metadata.
        total (int): Legacy total count
        items (list[CategoryListCompatResponseItemsItem] | Unset): List of categories
        categories (list[CategoryListCompatResponseCategoriesItem] | Unset): Legacy categories list
    """

    pagination: PaginationInfo
    total: int
    items: list[CategoryListCompatResponseItemsItem] | Unset = UNSET
    categories: list[CategoryListCompatResponseCategoriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        total = self.total

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "total": total,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_list_compat_response_categories_item import CategoryListCompatResponseCategoriesItem
        from ..models.category_list_compat_response_items_item import CategoryListCompatResponseItemsItem
        from ..models.pagination_info import PaginationInfo

        d = dict(src_dict)
        pagination = PaginationInfo.from_dict(d.pop("pagination"))

        total = d.pop("total")

        _items = d.pop("items", UNSET)
        items: list[CategoryListCompatResponseItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CategoryListCompatResponseItemsItem.from_dict(items_item_data)

                items.append(items_item)

        _categories = d.pop("categories", UNSET)
        categories: list[CategoryListCompatResponseCategoriesItem] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CategoryListCompatResponseCategoriesItem.from_dict(categories_item_data)

                categories.append(categories_item)

        category_list_compat_response = cls(
            pagination=pagination,
            total=total,
            items=items,
            categories=categories,
        )

        category_list_compat_response.additional_properties = d
        return category_list_compat_response

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
