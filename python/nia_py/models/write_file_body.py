from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_file_body_headers_type_0 import WriteFileBodyHeadersType0


T = TypeVar("T", bound="WriteFileBody")


@_attrs_define
class WriteFileBody:
    """
    Attributes:
        path (str):
        body (str):
        encoding (str | Unset):  Default: 'utf8'.
        language (None | str | Unset):
        headers (None | Unset | WriteFileBodyHeadersType0):
    """

    path: str
    body: str
    encoding: str | Unset = "utf8"
    language: None | str | Unset = UNSET
    headers: None | Unset | WriteFileBodyHeadersType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.write_file_body_headers_type_0 import WriteFileBodyHeadersType0

        path = self.path

        body = self.body

        encoding = self.encoding

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, WriteFileBodyHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "body": body,
            }
        )
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if language is not UNSET:
            field_dict["language"] = language
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.write_file_body_headers_type_0 import WriteFileBodyHeadersType0

        d = dict(src_dict)
        path = d.pop("path")

        body = d.pop("body")

        encoding = d.pop("encoding", UNSET)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_headers(data: object) -> None | Unset | WriteFileBodyHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = WriteFileBodyHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WriteFileBodyHeadersType0, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        write_file_body = cls(
            path=path,
            body=body,
            encoding=encoding,
            language=language,
            headers=headers,
        )

        write_file_body.additional_properties = d
        return write_file_body

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
