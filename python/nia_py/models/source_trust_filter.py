from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_trust_filter_minimum_trust_tier_type_0 import SourceTrustFilterMinimumTrustTierType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceTrustFilter")


@_attrs_define
class SourceTrustFilter:
    """Filtering preferences for trust-aware retrieval.

    Attributes:
        minimum_trust_tier (None | SourceTrustFilterMinimumTrustTierType0 | Unset): Only include sources at or above
            this effective trust tier
        verified_only (bool | Unset): Only include Nia-verified sources Default: False.
        require_overlay (bool | Unset): Only include sources with curated overlays Default: False.
    """

    minimum_trust_tier: None | SourceTrustFilterMinimumTrustTierType0 | Unset = UNSET
    verified_only: bool | Unset = False
    require_overlay: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minimum_trust_tier: None | str | Unset
        if isinstance(self.minimum_trust_tier, Unset):
            minimum_trust_tier = UNSET
        elif isinstance(self.minimum_trust_tier, SourceTrustFilterMinimumTrustTierType0):
            minimum_trust_tier = self.minimum_trust_tier.value
        else:
            minimum_trust_tier = self.minimum_trust_tier

        verified_only = self.verified_only

        require_overlay = self.require_overlay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minimum_trust_tier is not UNSET:
            field_dict["minimum_trust_tier"] = minimum_trust_tier
        if verified_only is not UNSET:
            field_dict["verified_only"] = verified_only
        if require_overlay is not UNSET:
            field_dict["require_overlay"] = require_overlay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_minimum_trust_tier(data: object) -> None | SourceTrustFilterMinimumTrustTierType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                minimum_trust_tier_type_0 = SourceTrustFilterMinimumTrustTierType0(data)

                return minimum_trust_tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceTrustFilterMinimumTrustTierType0 | Unset, data)

        minimum_trust_tier = _parse_minimum_trust_tier(d.pop("minimum_trust_tier", UNSET))

        verified_only = d.pop("verified_only", UNSET)

        require_overlay = d.pop("require_overlay", UNSET)

        source_trust_filter = cls(
            minimum_trust_tier=minimum_trust_tier,
            verified_only=verified_only,
            require_overlay=require_overlay,
        )

        source_trust_filter.additional_properties = d
        return source_trust_filter

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
