from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_interaction_request_action import SourceInteractionRequestAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceInteractionRequest")


@_attrs_define
class SourceInteractionRequest:
    """
    Attributes:
        chunk_id (str):
        action (SourceInteractionRequestAction):
        session_id (None | str | Unset):
        message_id (None | str | Unset):
        content_hash (None | str | Unset):
        retrieval_log_id (None | str | Unset):
        position_shown (int | None | Unset):
        dwell_time_ms (int | None | Unset):
    """

    chunk_id: str
    action: SourceInteractionRequestAction
    session_id: None | str | Unset = UNSET
    message_id: None | str | Unset = UNSET
    content_hash: None | str | Unset = UNSET
    retrieval_log_id: None | str | Unset = UNSET
    position_shown: int | None | Unset = UNSET
    dwell_time_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunk_id = self.chunk_id

        action = self.action.value

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        retrieval_log_id: None | str | Unset
        if isinstance(self.retrieval_log_id, Unset):
            retrieval_log_id = UNSET
        else:
            retrieval_log_id = self.retrieval_log_id

        position_shown: int | None | Unset
        if isinstance(self.position_shown, Unset):
            position_shown = UNSET
        else:
            position_shown = self.position_shown

        dwell_time_ms: int | None | Unset
        if isinstance(self.dwell_time_ms, Unset):
            dwell_time_ms = UNSET
        else:
            dwell_time_ms = self.dwell_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_id": chunk_id,
                "action": action,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if retrieval_log_id is not UNSET:
            field_dict["retrieval_log_id"] = retrieval_log_id
        if position_shown is not UNSET:
            field_dict["position_shown"] = position_shown
        if dwell_time_ms is not UNSET:
            field_dict["dwell_time_ms"] = dwell_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_id = d.pop("chunk_id")

        action = SourceInteractionRequestAction(d.pop("action"))

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_id = _parse_message_id(d.pop("message_id", UNSET))

        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("content_hash", UNSET))

        def _parse_retrieval_log_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retrieval_log_id = _parse_retrieval_log_id(d.pop("retrieval_log_id", UNSET))

        def _parse_position_shown(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_shown = _parse_position_shown(d.pop("position_shown", UNSET))

        def _parse_dwell_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dwell_time_ms = _parse_dwell_time_ms(d.pop("dwell_time_ms", UNSET))

        source_interaction_request = cls(
            chunk_id=chunk_id,
            action=action,
            session_id=session_id,
            message_id=message_id,
            content_hash=content_hash,
            retrieval_log_id=retrieval_log_id,
            position_shown=position_shown,
            dwell_time_ms=dwell_time_ms,
        )

        source_interaction_request.additional_properties = d
        return source_interaction_request

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
