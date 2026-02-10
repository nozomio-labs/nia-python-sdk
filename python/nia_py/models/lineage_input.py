from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineageInput")


@_attrs_define
class LineageInput:
    """Input model for lineage tracking.

    Attributes:
        source_ids (list[str] | Unset): Source identifiers (e.g., 'repo:owner/repo', 'doc:name')
        confidence (float | None | Unset): Confidence score 0-1
        derived_from (list[str] | None | Unset): Parent context IDs if derived
        tool_calls (list[str] | None | Unset): Tools used to create this artifact
        model_version (None | str | Unset): Model version that created this
    """

    source_ids: list[str] | Unset = UNSET
    confidence: float | None | Unset = UNSET
    derived_from: list[str] | None | Unset = UNSET
    tool_calls: list[str] | None | Unset = UNSET
    model_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = self.source_ids

        confidence: float | None | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        derived_from: list[str] | None | Unset
        if isinstance(self.derived_from, Unset):
            derived_from = UNSET
        elif isinstance(self.derived_from, list):
            derived_from = self.derived_from

        else:
            derived_from = self.derived_from

        tool_calls: list[str] | None | Unset
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        elif isinstance(self.tool_calls, list):
            tool_calls = self.tool_calls

        else:
            tool_calls = self.tool_calls

        model_version: None | str | Unset
        if isinstance(self.model_version, Unset):
            model_version = UNSET
        else:
            model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_ids is not UNSET:
            field_dict["source_ids"] = source_ids
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if derived_from is not UNSET:
            field_dict["derived_from"] = derived_from
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if model_version is not UNSET:
            field_dict["model_version"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_ids = cast(list[str], d.pop("source_ids", UNSET))

        def _parse_confidence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_derived_from(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                derived_from_type_0 = cast(list[str], data)

                return derived_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        derived_from = _parse_derived_from(d.pop("derived_from", UNSET))

        def _parse_tool_calls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = cast(list[str], data)

                return tool_calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tool_calls = _parse_tool_calls(d.pop("tool_calls", UNSET))

        def _parse_model_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_version = _parse_model_version(d.pop("model_version", UNSET))

        lineage_input = cls(
            source_ids=source_ids,
            confidence=confidence,
            derived_from=derived_from,
            tool_calls=tool_calls,
            model_version=model_version,
        )

        lineage_input.additional_properties = d
        return lineage_input

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
