from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.subscription_results import SubscriptionResults
    from ..models.subscription_summary import SubscriptionSummary


T = TypeVar("T", bound="SubscribeResponse")


@_attrs_define
class SubscribeResponse:
    """
    Attributes:
        manifest_type (str):
        total_dependencies (int):
        results (SubscriptionResults):
        summary (SubscriptionSummary):
    """

    manifest_type: str
    total_dependencies: int
    results: SubscriptionResults
    summary: SubscriptionSummary
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest_type = self.manifest_type

        total_dependencies = self.total_dependencies

        results = self.results.to_dict()

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manifest_type": manifest_type,
                "total_dependencies": total_dependencies,
                "results": results,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_results import SubscriptionResults
        from ..models.subscription_summary import SubscriptionSummary

        d = dict(src_dict)
        manifest_type = d.pop("manifest_type")

        total_dependencies = d.pop("total_dependencies")

        results = SubscriptionResults.from_dict(d.pop("results"))

        summary = SubscriptionSummary.from_dict(d.pop("summary"))

        subscribe_response = cls(
            manifest_type=manifest_type,
            total_dependencies=total_dependencies,
            results=results,
            summary=summary,
        )

        subscribe_response.additional_properties = d
        return subscribe_response

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
