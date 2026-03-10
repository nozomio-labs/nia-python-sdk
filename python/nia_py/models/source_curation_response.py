from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_curation_response_source_type import SourceCurationResponseSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_annotation import SourceAnnotation
    from ..models.source_curated_overlay import SourceCuratedOverlay
    from ..models.source_trust_signals import SourceTrustSignals


T = TypeVar("T", bound="SourceCurationResponse")


@_attrs_define
class SourceCurationResponse:
    """Full curation state for a source.

    Attributes:
        source_id (str): Source identifier
        source_type (SourceCurationResponseSourceType): Source type
        trust_signals (SourceTrustSignals | Unset): Trust and curation signals attached to a source.
        overlay (None | SourceCuratedOverlay | Unset): Curated overlay if present
        annotations (list[SourceAnnotation] | Unset): Saved annotations for the source
        created_at (None | str | Unset): Curation record creation timestamp (ISO)
        updated_at (None | str | Unset): Curation record update timestamp (ISO)
    """

    source_id: str
    source_type: SourceCurationResponseSourceType
    trust_signals: SourceTrustSignals | Unset = UNSET
    overlay: None | SourceCuratedOverlay | Unset = UNSET
    annotations: list[SourceAnnotation] | Unset = UNSET
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.source_curated_overlay import SourceCuratedOverlay

        source_id = self.source_id

        source_type = self.source_type.value

        trust_signals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trust_signals, Unset):
            trust_signals = self.trust_signals.to_dict()

        overlay: dict[str, Any] | None | Unset
        if isinstance(self.overlay, Unset):
            overlay = UNSET
        elif isinstance(self.overlay, SourceCuratedOverlay):
            overlay = self.overlay.to_dict()
        else:
            overlay = self.overlay

        annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_id": source_id,
                "source_type": source_type,
            }
        )
        if trust_signals is not UNSET:
            field_dict["trust_signals"] = trust_signals
        if overlay is not UNSET:
            field_dict["overlay"] = overlay
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_annotation import SourceAnnotation
        from ..models.source_curated_overlay import SourceCuratedOverlay
        from ..models.source_trust_signals import SourceTrustSignals

        d = dict(src_dict)
        source_id = d.pop("source_id")

        source_type = SourceCurationResponseSourceType(d.pop("source_type"))

        _trust_signals = d.pop("trust_signals", UNSET)
        trust_signals: SourceTrustSignals | Unset
        if isinstance(_trust_signals, Unset):
            trust_signals = UNSET
        else:
            trust_signals = SourceTrustSignals.from_dict(_trust_signals)

        def _parse_overlay(data: object) -> None | SourceCuratedOverlay | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overlay_type_0 = SourceCuratedOverlay.from_dict(data)

                return overlay_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceCuratedOverlay | Unset, data)

        overlay = _parse_overlay(d.pop("overlay", UNSET))

        _annotations = d.pop("annotations", UNSET)
        annotations: list[SourceAnnotation] | Unset = UNSET
        if _annotations is not UNSET:
            annotations = []
            for annotations_item_data in _annotations:
                annotations_item = SourceAnnotation.from_dict(annotations_item_data)

                annotations.append(annotations_item)

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        source_curation_response = cls(
            source_id=source_id,
            source_type=source_type,
            trust_signals=trust_signals,
            overlay=overlay,
            annotations=annotations,
            created_at=created_at,
            updated_at=updated_at,
        )

        source_curation_response.additional_properties = d
        return source_curation_response

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
