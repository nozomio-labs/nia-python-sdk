from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_curation_update_request_overlay_kind_type_0 import SourceCurationUpdateRequestOverlayKindType0
from ..models.source_curation_update_request_trust_level_type_0 import SourceCurationUpdateRequestTrustLevelType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceCurationUpdateRequest")


@_attrs_define
class SourceCurationUpdateRequest:
    """
    Attributes:
        trust_level (None | SourceCurationUpdateRequestTrustLevelType0 | Unset): Trust preference for this source
        overlay_kind (None | SourceCurationUpdateRequestOverlayKindType0 | Unset): Overlay provenance
        overlay_summary (None | str | Unset): Short curated source summary
        overlay_guidance (None | str | Unset): Longer guidance for coding agents
        recommended_queries (list[str] | None | Unset): Suggested prompts for this source
        clear_overlay (bool | Unset): Remove any existing curated overlay Default: False.
    """

    trust_level: None | SourceCurationUpdateRequestTrustLevelType0 | Unset = UNSET
    overlay_kind: None | SourceCurationUpdateRequestOverlayKindType0 | Unset = UNSET
    overlay_summary: None | str | Unset = UNSET
    overlay_guidance: None | str | Unset = UNSET
    recommended_queries: list[str] | None | Unset = UNSET
    clear_overlay: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trust_level: None | str | Unset
        if isinstance(self.trust_level, Unset):
            trust_level = UNSET
        elif isinstance(self.trust_level, SourceCurationUpdateRequestTrustLevelType0):
            trust_level = self.trust_level.value
        else:
            trust_level = self.trust_level

        overlay_kind: None | str | Unset
        if isinstance(self.overlay_kind, Unset):
            overlay_kind = UNSET
        elif isinstance(self.overlay_kind, SourceCurationUpdateRequestOverlayKindType0):
            overlay_kind = self.overlay_kind.value
        else:
            overlay_kind = self.overlay_kind

        overlay_summary: None | str | Unset
        if isinstance(self.overlay_summary, Unset):
            overlay_summary = UNSET
        else:
            overlay_summary = self.overlay_summary

        overlay_guidance: None | str | Unset
        if isinstance(self.overlay_guidance, Unset):
            overlay_guidance = UNSET
        else:
            overlay_guidance = self.overlay_guidance

        recommended_queries: list[str] | None | Unset
        if isinstance(self.recommended_queries, Unset):
            recommended_queries = UNSET
        elif isinstance(self.recommended_queries, list):
            recommended_queries = self.recommended_queries

        else:
            recommended_queries = self.recommended_queries

        clear_overlay = self.clear_overlay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trust_level is not UNSET:
            field_dict["trust_level"] = trust_level
        if overlay_kind is not UNSET:
            field_dict["overlay_kind"] = overlay_kind
        if overlay_summary is not UNSET:
            field_dict["overlay_summary"] = overlay_summary
        if overlay_guidance is not UNSET:
            field_dict["overlay_guidance"] = overlay_guidance
        if recommended_queries is not UNSET:
            field_dict["recommended_queries"] = recommended_queries
        if clear_overlay is not UNSET:
            field_dict["clear_overlay"] = clear_overlay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_trust_level(data: object) -> None | SourceCurationUpdateRequestTrustLevelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trust_level_type_0 = SourceCurationUpdateRequestTrustLevelType0(data)

                return trust_level_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceCurationUpdateRequestTrustLevelType0 | Unset, data)

        trust_level = _parse_trust_level(d.pop("trust_level", UNSET))

        def _parse_overlay_kind(data: object) -> None | SourceCurationUpdateRequestOverlayKindType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                overlay_kind_type_0 = SourceCurationUpdateRequestOverlayKindType0(data)

                return overlay_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceCurationUpdateRequestOverlayKindType0 | Unset, data)

        overlay_kind = _parse_overlay_kind(d.pop("overlay_kind", UNSET))

        def _parse_overlay_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_summary = _parse_overlay_summary(d.pop("overlay_summary", UNSET))

        def _parse_overlay_guidance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_guidance = _parse_overlay_guidance(d.pop("overlay_guidance", UNSET))

        def _parse_recommended_queries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recommended_queries_type_0 = cast(list[str], data)

                return recommended_queries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recommended_queries = _parse_recommended_queries(d.pop("recommended_queries", UNSET))

        clear_overlay = d.pop("clear_overlay", UNSET)

        source_curation_update_request = cls(
            trust_level=trust_level,
            overlay_kind=overlay_kind,
            overlay_summary=overlay_summary,
            overlay_guidance=overlay_guidance,
            recommended_queries=recommended_queries,
            clear_overlay=clear_overlay,
        )

        source_curation_update_request.additional_properties = d
        return source_curation_update_request

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
