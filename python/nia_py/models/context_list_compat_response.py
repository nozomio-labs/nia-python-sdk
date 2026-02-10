from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_list_compat_response_contexts_item import ContextListCompatResponseContextsItem
    from ..models.context_list_compat_response_items_item import ContextListCompatResponseItemsItem
    from ..models.pagination_info import PaginationInfo


T = TypeVar("T", bound="ContextListCompatResponse")


@_attrs_define
class ContextListCompatResponse:
    """Backwards-compatible context list response.

    Attributes:
        pagination (PaginationInfo): Pagination metadata.
        total (int): Legacy total count
        items (list[ContextListCompatResponseItemsItem] | Unset): List of contexts
        contexts (list[ContextListCompatResponseContextsItem] | Unset): Legacy contexts list
    """

    pagination: PaginationInfo
    total: int
    items: list[ContextListCompatResponseItemsItem] | Unset = UNSET
    contexts: list[ContextListCompatResponseContextsItem] | Unset = UNSET
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

        contexts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = []
            for contexts_item_data in self.contexts:
                contexts_item = contexts_item_data.to_dict()
                contexts.append(contexts_item)

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
        if contexts is not UNSET:
            field_dict["contexts"] = contexts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_list_compat_response_contexts_item import ContextListCompatResponseContextsItem
        from ..models.context_list_compat_response_items_item import ContextListCompatResponseItemsItem
        from ..models.pagination_info import PaginationInfo

        d = dict(src_dict)
        pagination = PaginationInfo.from_dict(d.pop("pagination"))

        total = d.pop("total")

        _items = d.pop("items", UNSET)
        items: list[ContextListCompatResponseItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ContextListCompatResponseItemsItem.from_dict(items_item_data)

                items.append(items_item)

        _contexts = d.pop("contexts", UNSET)
        contexts: list[ContextListCompatResponseContextsItem] | Unset = UNSET
        if _contexts is not UNSET:
            contexts = []
            for contexts_item_data in _contexts:
                contexts_item = ContextListCompatResponseContextsItem.from_dict(contexts_item_data)

                contexts.append(contexts_item)

        context_list_compat_response = cls(
            pagination=pagination,
            total=total,
            items=items,
            contexts=contexts,
        )

        context_list_compat_response.additional_properties = d
        return context_list_compat_response

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
