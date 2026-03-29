from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_query_request_json_schema_type_0 import DocumentQueryRequestJsonSchemaType0


T = TypeVar("T", bound="DocumentQueryRequest")


@_attrs_define
class DocumentQueryRequest:
    """Request for the v2 document/agent endpoint.

    Attributes:
        source_id (str): Data source ID of the indexed document
        query (str): Question to ask about the document
        json_schema (DocumentQueryRequestJsonSchemaType0 | None | Unset): JSON Schema for structured output
        model (str | Unset): Model to use (claude-opus-4-6-1m, claude-opus-4-6, claude-sonnet-4-5-20250929, etc.)
            Default: 'claude-opus-4-6-1m'.
        thinking_enabled (bool | Unset): Enable extended thinking Default: True.
        thinking_budget (int | Unset): Token budget for thinking (ignored for adaptive models like Opus 4.6) Default:
            10000.
        stream (bool | Unset): Stream response as SSE events Default: False.
    """

    source_id: str
    query: str
    json_schema: DocumentQueryRequestJsonSchemaType0 | None | Unset = UNSET
    model: str | Unset = "claude-opus-4-6-1m"
    thinking_enabled: bool | Unset = True
    thinking_budget: int | Unset = 10000
    stream: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_query_request_json_schema_type_0 import DocumentQueryRequestJsonSchemaType0

        source_id = self.source_id

        query = self.query

        json_schema: dict[str, Any] | None | Unset
        if isinstance(self.json_schema, Unset):
            json_schema = UNSET
        elif isinstance(self.json_schema, DocumentQueryRequestJsonSchemaType0):
            json_schema = self.json_schema.to_dict()
        else:
            json_schema = self.json_schema

        model = self.model

        thinking_enabled = self.thinking_enabled

        thinking_budget = self.thinking_budget

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_id": source_id,
                "query": query,
            }
        )
        if json_schema is not UNSET:
            field_dict["json_schema"] = json_schema
        if model is not UNSET:
            field_dict["model"] = model
        if thinking_enabled is not UNSET:
            field_dict["thinking_enabled"] = thinking_enabled
        if thinking_budget is not UNSET:
            field_dict["thinking_budget"] = thinking_budget
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_query_request_json_schema_type_0 import DocumentQueryRequestJsonSchemaType0

        d = dict(src_dict)
        source_id = d.pop("source_id")

        query = d.pop("query")

        def _parse_json_schema(data: object) -> DocumentQueryRequestJsonSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                json_schema_type_0 = DocumentQueryRequestJsonSchemaType0.from_dict(data)

                return json_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocumentQueryRequestJsonSchemaType0 | None | Unset, data)

        json_schema = _parse_json_schema(d.pop("json_schema", UNSET))

        model = d.pop("model", UNSET)

        thinking_enabled = d.pop("thinking_enabled", UNSET)

        thinking_budget = d.pop("thinking_budget", UNSET)

        stream = d.pop("stream", UNSET)

        document_query_request = cls(
            source_id=source_id,
            query=query,
            json_schema=json_schema,
            model=model,
            thinking_enabled=thinking_enabled,
            thinking_budget=thinking_budget,
            stream=stream,
        )

        document_query_request.additional_properties = d
        return document_query_request

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
