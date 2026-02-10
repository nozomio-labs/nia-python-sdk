from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionSummary")


@_attrs_define
class SubscriptionSummary:
    """
    Attributes:
        instant_access (int):
        wait_for_indexing (int):
        started_indexing (int):
        not_found (int):
        errors (int):
        skipped (int):
    """

    instant_access: int
    wait_for_indexing: int
    started_indexing: int
    not_found: int
    errors: int
    skipped: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instant_access = self.instant_access

        wait_for_indexing = self.wait_for_indexing

        started_indexing = self.started_indexing

        not_found = self.not_found

        errors = self.errors

        skipped = self.skipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instant_access": instant_access,
                "wait_for_indexing": wait_for_indexing,
                "started_indexing": started_indexing,
                "not_found": not_found,
                "errors": errors,
                "skipped": skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instant_access = d.pop("instant_access")

        wait_for_indexing = d.pop("wait_for_indexing")

        started_indexing = d.pop("started_indexing")

        not_found = d.pop("not_found")

        errors = d.pop("errors")

        skipped = d.pop("skipped")

        subscription_summary = cls(
            instant_access=instant_access,
            wait_for_indexing=wait_for_indexing,
            started_indexing=started_indexing,
            not_found=not_found,
            errors=errors,
            skipped=skipped,
        )

        subscription_summary.additional_properties = d
        return subscription_summary

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
