from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_trust_signals_scope import SourceTrustSignalsScope
from ..models.source_trust_signals_trust_level import SourceTrustSignalsTrustLevel
from ..models.source_trust_signals_trust_tier import SourceTrustSignalsTrustTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceTrustSignals")


@_attrs_define
class SourceTrustSignals:
    """Trust and curation signals attached to a source.

    Attributes:
        trust_level (SourceTrustSignalsTrustLevel | Unset): User or team trust preference for the source Default:
            SourceTrustSignalsTrustLevel.MEDIUM.
        trust_tier (SourceTrustSignalsTrustTier | Unset): Effective trust tier after derived verified/global signals
            Default: SourceTrustSignalsTrustTier.MEDIUM.
        scope (SourceTrustSignalsScope | Unset): Ownership scope of the source Default: SourceTrustSignalsScope.PRIVATE.
        is_global (bool | Unset): Whether the source references a shared global source Default: False.
        is_verified (bool | Unset): Whether the source has a Nia-verified overlay Default: False.
        overlay_available (bool | Unset): Whether a curated overlay is attached Default: False.
        annotation_count (int | Unset): Number of saved annotations for this source Default: 0.
    """

    trust_level: SourceTrustSignalsTrustLevel | Unset = SourceTrustSignalsTrustLevel.MEDIUM
    trust_tier: SourceTrustSignalsTrustTier | Unset = SourceTrustSignalsTrustTier.MEDIUM
    scope: SourceTrustSignalsScope | Unset = SourceTrustSignalsScope.PRIVATE
    is_global: bool | Unset = False
    is_verified: bool | Unset = False
    overlay_available: bool | Unset = False
    annotation_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trust_level: str | Unset = UNSET
        if not isinstance(self.trust_level, Unset):
            trust_level = self.trust_level.value

        trust_tier: str | Unset = UNSET
        if not isinstance(self.trust_tier, Unset):
            trust_tier = self.trust_tier.value

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        is_global = self.is_global

        is_verified = self.is_verified

        overlay_available = self.overlay_available

        annotation_count = self.annotation_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trust_level is not UNSET:
            field_dict["trust_level"] = trust_level
        if trust_tier is not UNSET:
            field_dict["trust_tier"] = trust_tier
        if scope is not UNSET:
            field_dict["scope"] = scope
        if is_global is not UNSET:
            field_dict["is_global"] = is_global
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if overlay_available is not UNSET:
            field_dict["overlay_available"] = overlay_available
        if annotation_count is not UNSET:
            field_dict["annotation_count"] = annotation_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _trust_level = d.pop("trust_level", UNSET)
        trust_level: SourceTrustSignalsTrustLevel | Unset
        if isinstance(_trust_level, Unset):
            trust_level = UNSET
        else:
            trust_level = SourceTrustSignalsTrustLevel(_trust_level)

        _trust_tier = d.pop("trust_tier", UNSET)
        trust_tier: SourceTrustSignalsTrustTier | Unset
        if isinstance(_trust_tier, Unset):
            trust_tier = UNSET
        else:
            trust_tier = SourceTrustSignalsTrustTier(_trust_tier)

        _scope = d.pop("scope", UNSET)
        scope: SourceTrustSignalsScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = SourceTrustSignalsScope(_scope)

        is_global = d.pop("is_global", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        overlay_available = d.pop("overlay_available", UNSET)

        annotation_count = d.pop("annotation_count", UNSET)

        source_trust_signals = cls(
            trust_level=trust_level,
            trust_tier=trust_tier,
            scope=scope,
            is_global=is_global,
            is_verified=is_verified,
            overlay_available=overlay_available,
            annotation_count=annotation_count,
        )

        source_trust_signals.additional_properties = d
        return source_trust_signals

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
