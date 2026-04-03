from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry_event import TelemetryEvent


T = TypeVar("T", bound="TelemetryPayload")


@_attrs_define
class TelemetryPayload:
    """
    Attributes:
        session_id (str):
        namespace (str):
        domain (str):
        url (str):
        mode (str):
        started_at (str):
        ended_at (str):
        file_count (int | Unset):  Default: 0.
        events (list[TelemetryEvent] | Unset):
    """

    session_id: str
    namespace: str
    domain: str
    url: str
    mode: str
    started_at: str
    ended_at: str
    file_count: int | Unset = 0
    events: list[TelemetryEvent] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        namespace = self.namespace

        domain = self.domain

        url = self.url

        mode = self.mode

        started_at = self.started_at

        ended_at = self.ended_at

        file_count = self.file_count

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "namespace": namespace,
                "domain": domain,
                "url": url,
                "mode": mode,
                "started_at": started_at,
                "ended_at": ended_at,
            }
        )
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.telemetry_event import TelemetryEvent

        d = dict(src_dict)
        session_id = d.pop("session_id")

        namespace = d.pop("namespace")

        domain = d.pop("domain")

        url = d.pop("url")

        mode = d.pop("mode")

        started_at = d.pop("started_at")

        ended_at = d.pop("ended_at")

        file_count = d.pop("file_count", UNSET)

        _events = d.pop("events", UNSET)
        events: list[TelemetryEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = TelemetryEvent.from_dict(events_item_data)

                events.append(events_item)

        telemetry_payload = cls(
            session_id=session_id,
            namespace=namespace,
            domain=domain,
            url=url,
            mode=mode,
            started_at=started_at,
            ended_at=ended_at,
            file_count=file_count,
            events=events,
        )

        telemetry_payload.additional_properties = d
        return telemetry_payload

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
