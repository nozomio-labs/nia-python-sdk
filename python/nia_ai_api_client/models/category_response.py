from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryResponse")


@_attrs_define
class CategoryResponse:
    """
    Attributes:
        id (str):
        name (str):
        user_id (str):
        created_at (str):
        updated_at (str):
        organization_id (None | str | Unset):
        color (None | str | Unset):
        order (int | Unset):  Default: 0.
    """

    id: str
    name: str
    user_id: str
    created_at: str
    updated_at: str
    organization_id: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id = self.user_id

        created_at = self.created_at

        updated_at = self.updated_at

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "user_id": user_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if color is not UNSET:
            field_dict["color"] = color
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        user_id = d.pop("user_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        order = d.pop("order", UNSET)

        category_response = cls(
            id=id,
            name=name,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            organization_id=organization_id,
            color=color,
            order=order,
        )

        category_response.additional_properties = d
        return category_response

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
