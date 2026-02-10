from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorResponse")


@_attrs_define
class AdvisorResponse:
    """Response model for advisor endpoint.

    Attributes:
        advice (str): Tailored advice
        sources_searched (int | Unset): Number of sources searched Default: 0.
        output_format (str | Unset):  Default: 'explanation'.
    """

    advice: str
    sources_searched: int | Unset = 0
    output_format: str | Unset = "explanation"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advice = self.advice

        sources_searched = self.sources_searched

        output_format = self.output_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "advice": advice,
            }
        )
        if sources_searched is not UNSET:
            field_dict["sources_searched"] = sources_searched
        if output_format is not UNSET:
            field_dict["output_format"] = output_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advice = d.pop("advice")

        sources_searched = d.pop("sources_searched", UNSET)

        output_format = d.pop("output_format", UNSET)

        advisor_response = cls(
            advice=advice,
            sources_searched=sources_searched,
            output_format=output_format,
        )

        advisor_response.additional_properties = d
        return advisor_response

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
