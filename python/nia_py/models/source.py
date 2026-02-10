from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_metadata import SourceMetadata


T = TypeVar("T", bound="Source")


@_attrs_define
class Source:
    """Unified source representation.

    Attributes:
        id (str): Source identifier
        type_ (SourceType): Source type
        identifier (None | str | Unset): Canonical identifier (repo slug, URL, or folder path)
        display_name (None | str | Unset): Human-readable name
        status (None | str | Unset): Indexing status
        created_at (None | str | Unset): Creation timestamp (ISO)
        updated_at (None | str | Unset): Last update timestamp (ISO)
        category_id (None | str | Unset): Category assignment
        is_global (bool | None | Unset): Whether the source is global/shared
        global_source_id (None | str | Unset): Global source ID if applicable
        global_namespace (None | str | Unset): Global namespace if applicable
        metadata (SourceMetadata | Unset): Type-specific metadata
    """

    id: str
    type_: SourceType
    identifier: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    is_global: bool | None | Unset = UNSET
    global_source_id: None | str | Unset = UNSET
    global_namespace: None | str | Unset = UNSET
    metadata: SourceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        is_global: bool | None | Unset
        if isinstance(self.is_global, Unset):
            is_global = UNSET
        else:
            is_global = self.is_global

        global_source_id: None | str | Unset
        if isinstance(self.global_source_id, Unset):
            global_source_id = UNSET
        else:
            global_source_id = self.global_source_id

        global_namespace: None | str | Unset
        if isinstance(self.global_namespace, Unset):
            global_namespace = UNSET
        else:
            global_namespace = self.global_namespace

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if is_global is not UNSET:
            field_dict["is_global"] = is_global
        if global_source_id is not UNSET:
            field_dict["global_source_id"] = global_source_id
        if global_namespace is not UNSET:
            field_dict["global_namespace"] = global_namespace
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_metadata import SourceMetadata

        d = dict(src_dict)
        id = d.pop("id")

        type_ = SourceType(d.pop("type"))

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_is_global(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_global = _parse_is_global(d.pop("is_global", UNSET))

        def _parse_global_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_source_id = _parse_global_source_id(d.pop("global_source_id", UNSET))

        def _parse_global_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_namespace = _parse_global_namespace(d.pop("global_namespace", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: SourceMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SourceMetadata.from_dict(_metadata)

        source = cls(
            id=id,
            type_=type_,
            identifier=identifier,
            display_name=display_name,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            category_id=category_id,
            is_global=is_global,
            global_source_id=global_source_id,
            global_namespace=global_namespace,
            metadata=metadata,
        )

        source.additional_properties = d
        return source

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
