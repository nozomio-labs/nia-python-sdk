from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_research_response_citations_type_0_item import DeepResearchResponseCitationsType0Item
    from ..models.deep_research_response_data_type_0 import DeepResearchResponseDataType0
    from ..models.deep_research_response_trace_type_0_item import DeepResearchResponseTraceType0Item


T = TypeVar("T", bound="DeepResearchResponse")


@_attrs_define
class DeepResearchResponse:
    """Response for deep research.

    Attributes:
        data (DeepResearchResponseDataType0 | list[Any] | None | Unset): Structured research data
        citations (list[DeepResearchResponseCitationsType0Item] | None | Unset): Citations with URLs
        status (str | Unset): Research task status Default: 'completed'.
        trace (list[DeepResearchResponseTraceType0Item] | None | Unset): Verbose trace events
    """

    data: DeepResearchResponseDataType0 | list[Any] | None | Unset = UNSET
    citations: list[DeepResearchResponseCitationsType0Item] | None | Unset = UNSET
    status: str | Unset = "completed"
    trace: list[DeepResearchResponseTraceType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deep_research_response_data_type_0 import DeepResearchResponseDataType0

        data: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, DeepResearchResponseDataType0):
            data = self.data.to_dict()
        elif isinstance(self.data, list):
            data = self.data

        else:
            data = self.data

        citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.citations, Unset):
            citations = UNSET
        elif isinstance(self.citations, list):
            citations = []
            for citations_type_0_item_data in self.citations:
                citations_type_0_item = citations_type_0_item_data.to_dict()
                citations.append(citations_type_0_item)

        else:
            citations = self.citations

        status = self.status

        trace: list[dict[str, Any]] | None | Unset
        if isinstance(self.trace, Unset):
            trace = UNSET
        elif isinstance(self.trace, list):
            trace = []
            for trace_type_0_item_data in self.trace:
                trace_type_0_item = trace_type_0_item_data.to_dict()
                trace.append(trace_type_0_item)

        else:
            trace = self.trace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if citations is not UNSET:
            field_dict["citations"] = citations
        if status is not UNSET:
            field_dict["status"] = status
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_research_response_citations_type_0_item import DeepResearchResponseCitationsType0Item
        from ..models.deep_research_response_data_type_0 import DeepResearchResponseDataType0
        from ..models.deep_research_response_trace_type_0_item import DeepResearchResponseTraceType0Item

        d = dict(src_dict)

        def _parse_data(data: object) -> DeepResearchResponseDataType0 | list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = DeepResearchResponseDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_1 = cast(list[Any], data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepResearchResponseDataType0 | list[Any] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_citations(data: object) -> list[DeepResearchResponseCitationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                citations_type_0 = []
                _citations_type_0 = data
                for citations_type_0_item_data in _citations_type_0:
                    citations_type_0_item = DeepResearchResponseCitationsType0Item.from_dict(citations_type_0_item_data)

                    citations_type_0.append(citations_type_0_item)

                return citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DeepResearchResponseCitationsType0Item] | None | Unset, data)

        citations = _parse_citations(d.pop("citations", UNSET))

        status = d.pop("status", UNSET)

        def _parse_trace(data: object) -> list[DeepResearchResponseTraceType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trace_type_0 = []
                _trace_type_0 = data
                for trace_type_0_item_data in _trace_type_0:
                    trace_type_0_item = DeepResearchResponseTraceType0Item.from_dict(trace_type_0_item_data)

                    trace_type_0.append(trace_type_0_item)

                return trace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DeepResearchResponseTraceType0Item] | None | Unset, data)

        trace = _parse_trace(d.pop("trace", UNSET))

        deep_research_response = cls(
            data=data,
            citations=citations,
            status=status,
            trace=trace,
        )

        deep_research_response.additional_properties = d
        return deep_research_response

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
