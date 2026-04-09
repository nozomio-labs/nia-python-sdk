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
        query (str): Question to ask about the document(s)
        source_id (None | str | Unset): Data source ID of a single indexed document
        source_ids (list[str] | None | Unset): List of data source IDs for multi-document queries (max 50)
        json_schema (DocumentQueryRequestJsonSchemaType0 | None | Unset): JSON Schema for structured output
        model (str | Unset): Model to use (claude-opus-4-6-1m, claude-opus-4-6, claude-sonnet-4-5-20250929, etc.)
            Default: 'claude-opus-4-6-1m'.
        thinking_enabled (bool | Unset): Enable extended thinking Default: True.
        thinking_budget (int | Unset): Token budget for thinking (ignored for adaptive models like Opus 4.6) Default:
            10000.
        stream (bool | Unset): Stream response as SSE events Default: False.
    """

    query: str
    source_id: None | str | Unset = UNSET
    source_ids: list[str] | None | Unset = UNSET
    json_schema: DocumentQueryRequestJsonSchemaType0 | None | Unset = UNSET
    model: str | Unset = "claude-opus-4-6-1m"
    thinking_enabled: bool | Unset = True
    thinking_budget: int | Unset = 10000
    stream: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_query_request_json_schema_type_0 import DocumentQueryRequestJsonSchemaType0

        query = self.query

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        source_ids: list[str] | None | Unset
        if isinstance(self.source_ids, Unset):
            source_ids = UNSET
        elif isinstance(self.source_ids, list):
            source_ids = self.source_ids

        else:
            source_ids = self.source_ids

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
                "query": query,
            }
        )
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_ids is not UNSET:
            field_dict["source_ids"] = source_ids
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
        query = d.pop("query")

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_source_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_ids_type_0 = cast(list[str], data)

                return source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_ids = _parse_source_ids(d.pop("source_ids", UNSET))

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
            query=query,
            source_id=source_id,
            source_ids=source_ids,
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
