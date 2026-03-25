from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extract_request_json_schema import ExtractRequestJsonSchema


T = TypeVar("T", bound="ExtractRequest")


@_attrs_define
class ExtractRequest:
    """
    Attributes:
        json_schema (ExtractRequestJsonSchema):
        url (None | str | Unset):
        source_id (None | str | Unset):
        page_range (None | str | Unset):
    """

    json_schema: ExtractRequestJsonSchema
    url: None | str | Unset = UNSET
    source_id: None | str | Unset = UNSET
    page_range: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_schema = self.json_schema.to_dict()

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        page_range: None | str | Unset
        if isinstance(self.page_range, Unset):
            page_range = UNSET
        else:
            page_range = self.page_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "json_schema": json_schema,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if page_range is not UNSET:
            field_dict["page_range"] = page_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extract_request_json_schema import ExtractRequestJsonSchema

        d = dict(src_dict)
        json_schema = ExtractRequestJsonSchema.from_dict(d.pop("json_schema"))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_page_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_range = _parse_page_range(d.pop("page_range", UNSET))

        extract_request = cls(
            json_schema=json_schema,
            url=url,
            source_id=source_id,
            page_range=page_range,
        )

        extract_request.additional_properties = d
        return extract_request

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
