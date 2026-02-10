from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_ls_item import DocLsItem


T = TypeVar("T", bound="DocLsResponse")


@_attrs_define
class DocLsResponse:
    """Response for documentation listing.

    Attributes:
        path (str): Current path
        success (bool | Unset): Whether the request succeeded Default: True.
        directories (list[str] | Unset): Subdirectories at this path
        files (list[str] | Unset): Files at this path
        total (int | Unset): Total items in this path Default: 0.
        items (list[DocLsItem] | None | Unset): Listed items (deprecated)
    """

    path: str
    success: bool | Unset = True
    directories: list[str] | Unset = UNSET
    files: list[str] | Unset = UNSET
    total: int | Unset = 0
    items: list[DocLsItem] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        success = self.success

        directories: list[str] | Unset = UNSET
        if not isinstance(self.directories, Unset):
            directories = self.directories

        files: list[str] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files

        total = self.total

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success
        if directories is not UNSET:
            field_dict["directories"] = directories
        if files is not UNSET:
            field_dict["files"] = files
        if total is not UNSET:
            field_dict["total"] = total
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.doc_ls_item import DocLsItem

        d = dict(src_dict)
        path = d.pop("path")

        success = d.pop("success", UNSET)

        directories = cast(list[str], d.pop("directories", UNSET))

        files = cast(list[str], d.pop("files", UNSET))

        total = d.pop("total", UNSET)

        def _parse_items(data: object) -> list[DocLsItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = DocLsItem.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DocLsItem] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        doc_ls_response = cls(
            path=path,
            success=success,
            directories=directories,
            files=files,
            total=total,
            items=items,
        )

        doc_ls_response.additional_properties = d
        return doc_ls_response

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
