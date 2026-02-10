from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.subscription_result_item import SubscriptionResultItem


T = TypeVar("T", bound="SubscriptionResults")


@_attrs_define
class SubscriptionResults:
    """
    Attributes:
        instant_access (list[SubscriptionResultItem]):
        wait_for_indexing (list[SubscriptionResultItem]):
        started_indexing (list[SubscriptionResultItem]):
        not_found (list[SubscriptionResultItem]):
        errors (list[SubscriptionResultItem]):
        skipped (list[SubscriptionResultItem]):
    """

    instant_access: list[SubscriptionResultItem]
    wait_for_indexing: list[SubscriptionResultItem]
    started_indexing: list[SubscriptionResultItem]
    not_found: list[SubscriptionResultItem]
    errors: list[SubscriptionResultItem]
    skipped: list[SubscriptionResultItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instant_access = []
        for instant_access_item_data in self.instant_access:
            instant_access_item = instant_access_item_data.to_dict()
            instant_access.append(instant_access_item)

        wait_for_indexing = []
        for wait_for_indexing_item_data in self.wait_for_indexing:
            wait_for_indexing_item = wait_for_indexing_item_data.to_dict()
            wait_for_indexing.append(wait_for_indexing_item)

        started_indexing = []
        for started_indexing_item_data in self.started_indexing:
            started_indexing_item = started_indexing_item_data.to_dict()
            started_indexing.append(started_indexing_item)

        not_found = []
        for not_found_item_data in self.not_found:
            not_found_item = not_found_item_data.to_dict()
            not_found.append(not_found_item)

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

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
        from ..models.subscription_result_item import SubscriptionResultItem

        d = dict(src_dict)
        instant_access = []
        _instant_access = d.pop("instant_access")
        for instant_access_item_data in _instant_access:
            instant_access_item = SubscriptionResultItem.from_dict(instant_access_item_data)

            instant_access.append(instant_access_item)

        wait_for_indexing = []
        _wait_for_indexing = d.pop("wait_for_indexing")
        for wait_for_indexing_item_data in _wait_for_indexing:
            wait_for_indexing_item = SubscriptionResultItem.from_dict(wait_for_indexing_item_data)

            wait_for_indexing.append(wait_for_indexing_item)

        started_indexing = []
        _started_indexing = d.pop("started_indexing")
        for started_indexing_item_data in _started_indexing:
            started_indexing_item = SubscriptionResultItem.from_dict(started_indexing_item_data)

            started_indexing.append(started_indexing_item)

        not_found = []
        _not_found = d.pop("not_found")
        for not_found_item_data in _not_found:
            not_found_item = SubscriptionResultItem.from_dict(not_found_item_data)

            not_found.append(not_found_item)

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = SubscriptionResultItem.from_dict(errors_item_data)

            errors.append(errors_item)

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = SubscriptionResultItem.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        subscription_results = cls(
            instant_access=instant_access,
            wait_for_indexing=wait_for_indexing,
            started_indexing=started_indexing,
            not_found=not_found,
            errors=errors,
            skipped=skipped,
        )

        subscription_results.additional_properties = d
        return subscription_results

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
