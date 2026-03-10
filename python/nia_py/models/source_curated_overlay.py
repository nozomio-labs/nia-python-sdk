from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_curated_overlay_kind import SourceCuratedOverlayKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceCuratedOverlay")


@_attrs_define
class SourceCuratedOverlay:
    """Structured high-confidence guidance layered on top of a source.

    Attributes:
        summary (str): Short high-confidence summary for the source
        kind (SourceCuratedOverlayKind | Unset): Overlay provenance Default: SourceCuratedOverlayKind.CUSTOM.
        guidance (None | str | Unset): Longer coding-agent guidance or caveats
        recommended_queries (list[str] | Unset): Suggested follow-up prompts for agents
        updated_at (None | str | Unset): Last overlay update timestamp (ISO)
    """

    summary: str
    kind: SourceCuratedOverlayKind | Unset = SourceCuratedOverlayKind.CUSTOM
    guidance: None | str | Unset = UNSET
    recommended_queries: list[str] | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        guidance: None | str | Unset
        if isinstance(self.guidance, Unset):
            guidance = UNSET
        else:
            guidance = self.guidance

        recommended_queries: list[str] | Unset = UNSET
        if not isinstance(self.recommended_queries, Unset):
            recommended_queries = self.recommended_queries

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if guidance is not UNSET:
            field_dict["guidance"] = guidance
        if recommended_queries is not UNSET:
            field_dict["recommended_queries"] = recommended_queries
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary")

        _kind = d.pop("kind", UNSET)
        kind: SourceCuratedOverlayKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = SourceCuratedOverlayKind(_kind)

        def _parse_guidance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guidance = _parse_guidance(d.pop("guidance", UNSET))

        recommended_queries = cast(list[str], d.pop("recommended_queries", UNSET))

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        source_curated_overlay = cls(
            summary=summary,
            kind=kind,
            guidance=guidance,
            recommended_queries=recommended_queries,
            updated_at=updated_at,
        )

        source_curated_overlay.additional_properties = d
        return source_curated_overlay

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
