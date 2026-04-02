from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_citation import DocumentCitation
    from ..models.document_query_response_structured_output_type_0 import DocumentQueryResponseStructuredOutputType0
    from ..models.document_query_response_usage_type_0 import DocumentQueryResponseUsageType0


T = TypeVar("T", bound="DocumentQueryResponse")


@_attrs_define
class DocumentQueryResponse:
    """Response from the v2 document/agent endpoint.

    Attributes:
        answer (str):
        model (str):
        citations (list[DocumentCitation] | Unset):
        structured_output (DocumentQueryResponseStructuredOutputType0 | list[Any] | None | Unset):
        usage (DocumentQueryResponseUsageType0 | None | Unset):
    """

    answer: str
    model: str
    citations: list[DocumentCitation] | Unset = UNSET
    structured_output: DocumentQueryResponseStructuredOutputType0 | list[Any] | None | Unset = UNSET
    usage: DocumentQueryResponseUsageType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_query_response_structured_output_type_0 import DocumentQueryResponseStructuredOutputType0
        from ..models.document_query_response_usage_type_0 import DocumentQueryResponseUsageType0

        answer = self.answer

        model = self.model

        citations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.citations, Unset):
            citations = []
            for citations_item_data in self.citations:
                citations_item = citations_item_data.to_dict()
                citations.append(citations_item)

        structured_output: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.structured_output, Unset):
            structured_output = UNSET
        elif isinstance(self.structured_output, DocumentQueryResponseStructuredOutputType0):
            structured_output = self.structured_output.to_dict()
        elif isinstance(self.structured_output, list):
            structured_output = self.structured_output

        else:
            structured_output = self.structured_output

        usage: dict[str, Any] | None | Unset
        if isinstance(self.usage, Unset):
            usage = UNSET
        elif isinstance(self.usage, DocumentQueryResponseUsageType0):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answer": answer,
                "model": model,
            }
        )
        if citations is not UNSET:
            field_dict["citations"] = citations
        if structured_output is not UNSET:
            field_dict["structured_output"] = structured_output
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_citation import DocumentCitation
        from ..models.document_query_response_structured_output_type_0 import DocumentQueryResponseStructuredOutputType0
        from ..models.document_query_response_usage_type_0 import DocumentQueryResponseUsageType0

        d = dict(src_dict)
        answer = d.pop("answer")

        model = d.pop("model")

        _citations = d.pop("citations", UNSET)
        citations: list[DocumentCitation] | Unset = UNSET
        if _citations is not UNSET:
            citations = []
            for citations_item_data in _citations:
                citations_item = DocumentCitation.from_dict(citations_item_data)

                citations.append(citations_item)

        def _parse_structured_output(
            data: object,
        ) -> DocumentQueryResponseStructuredOutputType0 | list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                structured_output_type_0 = DocumentQueryResponseStructuredOutputType0.from_dict(data)

                return structured_output_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                structured_output_type_1 = cast(list[Any], data)

                return structured_output_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocumentQueryResponseStructuredOutputType0 | list[Any] | None | Unset, data)

        structured_output = _parse_structured_output(d.pop("structured_output", UNSET))

        def _parse_usage(data: object) -> DocumentQueryResponseUsageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = DocumentQueryResponseUsageType0.from_dict(data)

                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocumentQueryResponseUsageType0 | None | Unset, data)

        usage = _parse_usage(d.pop("usage", UNSET))

        document_query_response = cls(
            answer=answer,
            model=model,
            citations=citations,
            structured_output=structured_output,
            usage=usage,
        )

        document_query_response.additional_properties = d
        return document_query_response

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
