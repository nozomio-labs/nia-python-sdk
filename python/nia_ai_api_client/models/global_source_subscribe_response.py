from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalSourceSubscribeResponse")


@_attrs_define
class GlobalSourceSubscribeResponse:
    """Response model for global source subscription

    Attributes:
        action (str): Action taken: instant_access | wait_for_indexing | not_indexed | use_private | indexing_started
        message (str): Human-readable description of the action
        global_source_id (None | str | Unset): Canonical ID of the global source
        namespace (None | str | Unset): TurboPuffer namespace for the source
        status (None | str | Unset): Current status of the global source
        local_reference_id (None | str | Unset): ID of the created local reference (project/data_source)
        display_name (None | str | Unset): Display name of the source
    """

    action: str
    message: str
    global_source_id: None | str | Unset = UNSET
    namespace: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    local_reference_id: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        message = self.message

        global_source_id: None | str | Unset
        if isinstance(self.global_source_id, Unset):
            global_source_id = UNSET
        else:
            global_source_id = self.global_source_id

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        local_reference_id: None | str | Unset
        if isinstance(self.local_reference_id, Unset):
            local_reference_id = UNSET
        else:
            local_reference_id = self.local_reference_id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "message": message,
            }
        )
        if global_source_id is not UNSET:
            field_dict["global_source_id"] = global_source_id
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if status is not UNSET:
            field_dict["status"] = status
        if local_reference_id is not UNSET:
            field_dict["local_reference_id"] = local_reference_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        message = d.pop("message")

        def _parse_global_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_source_id = _parse_global_source_id(d.pop("global_source_id", UNSET))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_local_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_reference_id = _parse_local_reference_id(d.pop("local_reference_id", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        global_source_subscribe_response = cls(
            action=action,
            message=message,
            global_source_id=global_source_id,
            namespace=namespace,
            status=status,
            local_reference_id=local_reference_id,
            display_name=display_name,
        )

        global_source_subscribe_response.additional_properties = d
        return global_source_subscribe_response

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
