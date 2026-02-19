from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DailyUsage1MResponse")


@_attrs_define
class DailyUsage1MResponse:
    """
    Attributes:
        used (int): Number of 1M context requests used today
        limit (int): Daily limit for 1M context requests
        remaining (int): Remaining 1M context requests today
    """

    used: int
    limit: int
    remaining: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        limit = self.limit

        remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "limit": limit,
                "remaining": remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used")

        limit = d.pop("limit")

        remaining = d.pop("remaining")

        daily_usage_1m_response = cls(
            used=used,
            limit=limit,
            remaining=remaining,
        )

        daily_usage_1m_response.additional_properties = d
        return daily_usage_1m_response

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
