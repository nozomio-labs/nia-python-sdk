from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDriveIndexRequest")


@_attrs_define
class GoogleDriveIndexRequest:
    """
    Attributes:
        file_ids (list[str] | Unset): Drive file IDs to index
        folder_ids (list[str] | Unset): Drive folder IDs to index
        display_name (None | str | Unset): Optional custom display name for the indexed Drive source
    """

    file_ids: list[str] | Unset = UNSET
    folder_ids: list[str] | Unset = UNSET
    display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        folder_ids: list[str] | Unset = UNSET
        if not isinstance(self.folder_ids, Unset):
            folder_ids = self.folder_ids

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if folder_ids is not UNSET:
            field_dict["folder_ids"] = folder_ids
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        folder_ids = cast(list[str], d.pop("folder_ids", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        google_drive_index_request = cls(
            file_ids=file_ids,
            folder_ids=folder_ids,
            display_name=display_name,
        )

        google_drive_index_request.additional_properties = d
        return google_drive_index_request

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
