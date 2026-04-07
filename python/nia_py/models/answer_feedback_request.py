from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.answer_feedback_request_signal import AnswerFeedbackRequestSignal
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnswerFeedbackRequest")


@_attrs_define
class AnswerFeedbackRequest:
    """
    Attributes:
        signal (AnswerFeedbackRequestSignal):
        session_id (None | str | Unset):
        message_id (None | str | Unset):
        retrieval_log_id (None | str | Unset):
        comment (None | str | Unset):
    """

    signal: AnswerFeedbackRequestSignal
    session_id: None | str | Unset = UNSET
    message_id: None | str | Unset = UNSET
    retrieval_log_id: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal = self.signal.value

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

        retrieval_log_id: None | str | Unset
        if isinstance(self.retrieval_log_id, Unset):
            retrieval_log_id = UNSET
        else:
            retrieval_log_id = self.retrieval_log_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signal": signal,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if retrieval_log_id is not UNSET:
            field_dict["retrieval_log_id"] = retrieval_log_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signal = AnswerFeedbackRequestSignal(d.pop("signal"))

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

        def _parse_retrieval_log_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retrieval_log_id = _parse_retrieval_log_id(d.pop("retrieval_log_id", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        answer_feedback_request = cls(
            signal=signal,
            session_id=session_id,
            message_id=message_id,
            retrieval_log_id=retrieval_log_id,
            comment=comment,
        )

        answer_feedback_request.additional_properties = d
        return answer_feedback_request

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
