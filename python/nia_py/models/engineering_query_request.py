from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engineering_query_request_conversation_history_item import (
        EngineeringQueryRequestConversationHistoryItem,
    )


T = TypeVar("T", bound="EngineeringQueryRequest")


@_attrs_define
class EngineeringQueryRequest:
    """
    Attributes:
        query (str):
        conversation_history (list[EngineeringQueryRequestConversationHistoryItem] | Unset):
    """

    query: str
    conversation_history: list[EngineeringQueryRequestConversationHistoryItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        conversation_history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conversation_history, Unset):
            conversation_history = []
            for conversation_history_item_data in self.conversation_history:
                conversation_history_item = conversation_history_item_data.to_dict()
                conversation_history.append(conversation_history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if conversation_history is not UNSET:
            field_dict["conversation_history"] = conversation_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engineering_query_request_conversation_history_item import (
            EngineeringQueryRequestConversationHistoryItem,
        )

        d = dict(src_dict)
        query = d.pop("query")

        _conversation_history = d.pop("conversation_history", UNSET)
        conversation_history: list[EngineeringQueryRequestConversationHistoryItem] | Unset = UNSET
        if _conversation_history is not UNSET:
            conversation_history = []
            for conversation_history_item_data in _conversation_history:
                conversation_history_item = EngineeringQueryRequestConversationHistoryItem.from_dict(
                    conversation_history_item_data
                )

                conversation_history.append(conversation_history_item)

        engineering_query_request = cls(
            query=query,
            conversation_history=conversation_history,
        )

        engineering_query_request.additional_properties = d
        return engineering_query_request

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
