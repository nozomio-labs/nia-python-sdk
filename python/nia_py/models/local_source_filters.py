from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalSourceFilters")


@_attrs_define
class LocalSourceFilters:
    """Filters for local/personal source retrieval (messages, contacts, etc.).

    Attributes:
        source_subtype (None | str | Unset): Filter by source subtype (e.g., 'database', 'telegram_export')
        db_type (None | str | Unset): Filter by database type (e.g., 'imessage', 'telegram', 'safari_history')
        connector_type (None | str | Unset): Filter by connector type (e.g., 'imessage', 'whatsapp', 'contacts')
        conversation_id (None | str | Unset): Filter to a specific conversation/chat
        contact_id (None | str | Unset): Filter to messages with a specific contact
        sender_role (None | str | Unset): Filter by sender role: 'self' or 'contact'
        time_after (None | str | Unset): Only return results with timestamp after this ISO datetime
        time_before (None | str | Unset): Only return results with timestamp before this ISO datetime
    """

    source_subtype: None | str | Unset = UNSET
    db_type: None | str | Unset = UNSET
    connector_type: None | str | Unset = UNSET
    conversation_id: None | str | Unset = UNSET
    contact_id: None | str | Unset = UNSET
    sender_role: None | str | Unset = UNSET
    time_after: None | str | Unset = UNSET
    time_before: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_subtype: None | str | Unset
        if isinstance(self.source_subtype, Unset):
            source_subtype = UNSET
        else:
            source_subtype = self.source_subtype

        db_type: None | str | Unset
        if isinstance(self.db_type, Unset):
            db_type = UNSET
        else:
            db_type = self.db_type

        connector_type: None | str | Unset
        if isinstance(self.connector_type, Unset):
            connector_type = UNSET
        else:
            connector_type = self.connector_type

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        sender_role: None | str | Unset
        if isinstance(self.sender_role, Unset):
            sender_role = UNSET
        else:
            sender_role = self.sender_role

        time_after: None | str | Unset
        if isinstance(self.time_after, Unset):
            time_after = UNSET
        else:
            time_after = self.time_after

        time_before: None | str | Unset
        if isinstance(self.time_before, Unset):
            time_before = UNSET
        else:
            time_before = self.time_before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_subtype is not UNSET:
            field_dict["source_subtype"] = source_subtype
        if db_type is not UNSET:
            field_dict["db_type"] = db_type
        if connector_type is not UNSET:
            field_dict["connector_type"] = connector_type
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if sender_role is not UNSET:
            field_dict["sender_role"] = sender_role
        if time_after is not UNSET:
            field_dict["time_after"] = time_after
        if time_before is not UNSET:
            field_dict["time_before"] = time_before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_source_subtype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_subtype = _parse_source_subtype(d.pop("source_subtype", UNSET))

        def _parse_db_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        db_type = _parse_db_type(d.pop("db_type", UNSET))

        def _parse_connector_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connector_type = _parse_connector_type(d.pop("connector_type", UNSET))

        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversation_id", UNSET))

        def _parse_contact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_id = _parse_contact_id(d.pop("contact_id", UNSET))

        def _parse_sender_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_role = _parse_sender_role(d.pop("sender_role", UNSET))

        def _parse_time_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_after = _parse_time_after(d.pop("time_after", UNSET))

        def _parse_time_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_before = _parse_time_before(d.pop("time_before", UNSET))

        local_source_filters = cls(
            source_subtype=source_subtype,
            db_type=db_type,
            connector_type=connector_type,
            conversation_id=conversation_id,
            contact_id=contact_id,
            sender_role=sender_role,
            time_after=time_after,
            time_before=time_before,
        )

        local_source_filters.additional_properties = d
        return local_source_filters

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
