from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepResearchRequestWithMode")


@_attrs_define
class DeepResearchRequestWithMode:
    """
    Attributes:
        query (str): Research question
        output_format (None | str | Unset): Optional structure hint
        verbose (bool | Unset): Include verbose trace output Default: False.
        mode (Literal['deep'] | Unset): Search mode discriminator Default: 'deep'.
    """

    query: str
    output_format: None | str | Unset = UNSET
    verbose: bool | Unset = False
    mode: Literal["deep"] | Unset = "deep"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        output_format: None | str | Unset
        if isinstance(self.output_format, Unset):
            output_format = UNSET
        else:
            output_format = self.output_format

        verbose = self.verbose

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_output_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_format = _parse_output_format(d.pop("output_format", UNSET))

        verbose = d.pop("verbose", UNSET)

        mode = cast(Literal["deep"] | Unset, d.pop("mode", UNSET))
        if mode != "deep" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'deep', got '{mode}'")

        deep_research_request_with_mode = cls(
            query=query,
            output_format=output_format,
            verbose=verbose,
            mode=mode,
        )

        deep_research_request_with_mode.additional_properties = d
        return deep_research_request_with_mode

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
