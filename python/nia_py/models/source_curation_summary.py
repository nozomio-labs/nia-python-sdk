from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_trust_signals import SourceTrustSignals


T = TypeVar("T", bound="SourceCurationSummary")


@_attrs_define
class SourceCurationSummary:
    """Compact curation info embedded into source responses.

    Attributes:
        trust_signals (SourceTrustSignals | Unset): Trust and curation signals attached to a source.
        overlay_summary (None | str | Unset): Short overlay summary if one exists
        recommended_queries (list[str] | Unset): Suggested prompts from the overlay
    """

    trust_signals: SourceTrustSignals | Unset = UNSET
    overlay_summary: None | str | Unset = UNSET
    recommended_queries: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trust_signals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trust_signals, Unset):
            trust_signals = self.trust_signals.to_dict()

        overlay_summary: None | str | Unset
        if isinstance(self.overlay_summary, Unset):
            overlay_summary = UNSET
        else:
            overlay_summary = self.overlay_summary

        recommended_queries: list[str] | Unset = UNSET
        if not isinstance(self.recommended_queries, Unset):
            recommended_queries = self.recommended_queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trust_signals is not UNSET:
            field_dict["trust_signals"] = trust_signals
        if overlay_summary is not UNSET:
            field_dict["overlay_summary"] = overlay_summary
        if recommended_queries is not UNSET:
            field_dict["recommended_queries"] = recommended_queries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_trust_signals import SourceTrustSignals

        d = dict(src_dict)
        _trust_signals = d.pop("trust_signals", UNSET)
        trust_signals: SourceTrustSignals | Unset
        if isinstance(_trust_signals, Unset):
            trust_signals = UNSET
        else:
            trust_signals = SourceTrustSignals.from_dict(_trust_signals)

        def _parse_overlay_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_summary = _parse_overlay_summary(d.pop("overlay_summary", UNSET))

        recommended_queries = cast(list[str], d.pop("recommended_queries", UNSET))

        source_curation_summary = cls(
            trust_signals=trust_signals,
            overlay_summary=overlay_summary,
            recommended_queries=recommended_queries,
        )

        source_curation_summary.additional_properties = d
        return source_curation_summary

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
