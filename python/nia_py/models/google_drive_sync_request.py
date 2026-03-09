from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDriveSyncRequest")


@_attrs_define
class GoogleDriveSyncRequest:
    """
    Attributes:
        force_full (bool | Unset): Force a full rebuild instead of incremental sync Default: False.
        scope_ids (list[str] | Unset): Optional sync scope IDs to limit the sync run
    """

    force_full: bool | Unset = False
    scope_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force_full = self.force_full

        scope_ids: list[str] | Unset = UNSET
        if not isinstance(self.scope_ids, Unset):
            scope_ids = self.scope_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force_full is not UNSET:
            field_dict["force_full"] = force_full
        if scope_ids is not UNSET:
            field_dict["scope_ids"] = scope_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        force_full = d.pop("force_full", UNSET)

        scope_ids = cast(list[str], d.pop("scope_ids", UNSET))

        google_drive_sync_request = cls(
            force_full=force_full,
            scope_ids=scope_ids,
        )

        google_drive_sync_request.additional_properties = d
        return google_drive_sync_request

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
