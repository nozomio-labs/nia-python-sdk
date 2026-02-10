from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionResultItem")


@_attrs_define
class SubscriptionResultItem:
    """
    Attributes:
        name (str):
        action (str):
        docs_url (None | str):
        global_source_id (None | str):
        namespace (None | str):
        message (str):
    """

    name: str
    action: str
    docs_url: None | str
    global_source_id: None | str
    namespace: None | str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action = self.action

        docs_url: None | str
        docs_url = self.docs_url

        global_source_id: None | str
        global_source_id = self.global_source_id

        namespace: None | str
        namespace = self.namespace

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action": action,
                "docs_url": docs_url,
                "global_source_id": global_source_id,
                "namespace": namespace,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        action = d.pop("action")

        def _parse_docs_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        docs_url = _parse_docs_url(d.pop("docs_url"))

        def _parse_global_source_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        global_source_id = _parse_global_source_id(d.pop("global_source_id"))

        def _parse_namespace(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        namespace = _parse_namespace(d.pop("namespace"))

        message = d.pop("message")

        subscription_result_item = cls(
            name=name,
            action=action,
            docs_url=docs_url,
            global_source_id=global_source_id,
            namespace=namespace,
            message=message,
        )

        subscription_result_item.additional_properties = d
        return subscription_result_item

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
