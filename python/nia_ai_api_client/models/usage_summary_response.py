from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_summary_response_usage import UsageSummaryResponseUsage


T = TypeVar("T", bound="UsageSummaryResponse")


@_attrs_define
class UsageSummaryResponse:
    """Response for usage summary.

    Attributes:
        user_id (str): User identifier
        billing_period_start (datetime.datetime): Start of current billing period
        billing_period_end (datetime.datetime): End of current billing period
        organization_id (None | str | Unset): Organization identifier (if applicable)
        subscription_tier (str | Unset): Current subscription tier Default: 'free'.
        usage (UsageSummaryResponseUsage | Unset): Usage breakdown by operation type
    """

    user_id: str
    billing_period_start: datetime.datetime
    billing_period_end: datetime.datetime
    organization_id: None | str | Unset = UNSET
    subscription_tier: str | Unset = "free"
    usage: UsageSummaryResponseUsage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        billing_period_start = self.billing_period_start.isoformat()

        billing_period_end = self.billing_period_end.isoformat()

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        subscription_tier = self.subscription_tier

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "billing_period_start": billing_period_start,
                "billing_period_end": billing_period_end,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if subscription_tier is not UNSET:
            field_dict["subscription_tier"] = subscription_tier
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_summary_response_usage import UsageSummaryResponseUsage

        d = dict(src_dict)
        user_id = d.pop("user_id")

        billing_period_start = isoparse(d.pop("billing_period_start"))

        billing_period_end = isoparse(d.pop("billing_period_end"))

        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        subscription_tier = d.pop("subscription_tier", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: UsageSummaryResponseUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = UsageSummaryResponseUsage.from_dict(_usage)

        usage_summary_response = cls(
            user_id=user_id,
            billing_period_start=billing_period_start,
            billing_period_end=billing_period_end,
            organization_id=organization_id,
            subscription_tier=subscription_tier,
            usage=usage,
        )

        usage_summary_response.additional_properties = d
        return usage_summary_response

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
