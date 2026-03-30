from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detect_response_result_type_0 import DetectResponseResultType0


T = TypeVar("T", bound="DetectResponse")


@_attrs_define
class DetectResponse:
    """
    Attributes:
        id (str):
        status (str):
        created_at (str):
        updated_at (str):
        progress (int | Unset):  Default: 0.
        type_ (str | Unset):  Default: 'detect'.
        url (None | str | Unset):
        source_display_name (None | str | Unset):
        page_range (None | str | Unset):
        result (DetectResponseResultType0 | None | Unset):
        page_count (int | Unset):  Default: 0.
        error (None | str | Unset):
    """

    id: str
    status: str
    created_at: str
    updated_at: str
    progress: int | Unset = 0
    type_: str | Unset = "detect"
    url: None | str | Unset = UNSET
    source_display_name: None | str | Unset = UNSET
    page_range: None | str | Unset = UNSET
    result: DetectResponseResultType0 | None | Unset = UNSET
    page_count: int | Unset = 0
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.detect_response_result_type_0 import DetectResponseResultType0

        id = self.id

        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        progress = self.progress

        type_ = self.type_

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source_display_name: None | str | Unset
        if isinstance(self.source_display_name, Unset):
            source_display_name = UNSET
        else:
            source_display_name = self.source_display_name

        page_range: None | str | Unset
        if isinstance(self.page_range, Unset):
            page_range = UNSET
        else:
            page_range = self.page_range

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, DetectResponseResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        page_count = self.page_count

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if progress is not UNSET:
            field_dict["progress"] = progress
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if source_display_name is not UNSET:
            field_dict["source_display_name"] = source_display_name
        if page_range is not UNSET:
            field_dict["page_range"] = page_range
        if result is not UNSET:
            field_dict["result"] = result
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detect_response_result_type_0 import DetectResponseResultType0

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        progress = d.pop("progress", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_source_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_display_name = _parse_source_display_name(d.pop("source_display_name", UNSET))

        def _parse_page_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_range = _parse_page_range(d.pop("page_range", UNSET))

        def _parse_result(data: object) -> DetectResponseResultType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = DetectResponseResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DetectResponseResultType0 | None | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        page_count = d.pop("page_count", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        detect_response = cls(
            id=id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            progress=progress,
            type_=type_,
            url=url,
            source_display_name=source_display_name,
            page_range=page_range,
            result=result,
            page_count=page_count,
            error=error,
        )

        detect_response.additional_properties = d
        return detect_response

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
