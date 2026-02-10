from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_delete_result import BulkDeleteResult


T = TypeVar("T", bound="BulkDeleteResponse")


@_attrs_define
class BulkDeleteResponse:
    """Response for bulk deletion

    Attributes:
        deleted (int): Number of successfully deleted items
        failed (int): Number of failed deletions
        results (list[BulkDeleteResult]): Per-item results
    """

    deleted: int
    failed: int
    results: list[BulkDeleteResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        failed = self.failed

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "failed": failed,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_delete_result import BulkDeleteResult

        d = dict(src_dict)
        deleted = d.pop("deleted")

        failed = d.pop("failed")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BulkDeleteResult.from_dict(results_item_data)

            results.append(results_item)

        bulk_delete_response = cls(
            deleted=deleted,
            failed=failed,
            results=results,
        )

        bulk_delete_response.additional_properties = d
        return bulk_delete_response

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
