from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HuggingFaceDatasetListItem")


@_attrs_define
class HuggingFaceDatasetListItem:
    """Response model for HuggingFace dataset list items.

    Attributes:
        id (str):
        status (str):
        dataset_id (None | str | Unset):
        url (None | str | Unset):
        source_type (str | Unset):  Default: 'huggingface_dataset'.
        is_active (bool | Unset):  Default: True.
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        chunk_count (int | None | Unset):
        display_name (None | str | Unset):
        owner (None | str | Unset):
        description (None | str | Unset):
        splits (list[str] | None | Unset):
        row_count (int | None | Unset):
        indexed_row_count (int | None | Unset):
        sampling_strategy (None | str | Unset):
        error (None | str | Unset):
    """

    id: str
    status: str
    dataset_id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    source_type: str | Unset = "huggingface_dataset"
    is_active: bool | Unset = True
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    chunk_count: int | None | Unset = UNSET
    display_name: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    splits: list[str] | None | Unset = UNSET
    row_count: int | None | Unset = UNSET
    indexed_row_count: int | None | Unset = UNSET
    sampling_strategy: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        dataset_id: None | str | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = self.dataset_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source_type = self.source_type

        is_active = self.is_active

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        chunk_count: int | None | Unset
        if isinstance(self.chunk_count, Unset):
            chunk_count = UNSET
        else:
            chunk_count = self.chunk_count

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        splits: list[str] | None | Unset
        if isinstance(self.splits, Unset):
            splits = UNSET
        elif isinstance(self.splits, list):
            splits = self.splits

        else:
            splits = self.splits

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        indexed_row_count: int | None | Unset
        if isinstance(self.indexed_row_count, Unset):
            indexed_row_count = UNSET
        else:
            indexed_row_count = self.indexed_row_count

        sampling_strategy: None | str | Unset
        if isinstance(self.sampling_strategy, Unset):
            sampling_strategy = UNSET
        else:
            sampling_strategy = self.sampling_strategy

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if url is not UNSET:
            field_dict["url"] = url
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if chunk_count is not UNSET:
            field_dict["chunk_count"] = chunk_count
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if description is not UNSET:
            field_dict["description"] = description
        if splits is not UNSET:
            field_dict["splits"] = splits
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if indexed_row_count is not UNSET:
            field_dict["indexed_row_count"] = indexed_row_count
        if sampling_strategy is not UNSET:
            field_dict["sampling_strategy"] = sampling_strategy
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        def _parse_dataset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_id = _parse_dataset_id(d.pop("dataset_id", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        source_type = d.pop("source_type", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_chunk_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_count = _parse_chunk_count(d.pop("chunk_count", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_splits(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = cast(list[str], data)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        splits = _parse_splits(d.pop("splits", UNSET))

        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        def _parse_indexed_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        indexed_row_count = _parse_indexed_row_count(d.pop("indexed_row_count", UNSET))

        def _parse_sampling_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sampling_strategy = _parse_sampling_strategy(d.pop("sampling_strategy", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        hugging_face_dataset_list_item = cls(
            id=id,
            status=status,
            dataset_id=dataset_id,
            url=url,
            source_type=source_type,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            chunk_count=chunk_count,
            display_name=display_name,
            owner=owner,
            description=description,
            splits=splits,
            row_count=row_count,
            indexed_row_count=indexed_row_count,
            sampling_strategy=sampling_strategy,
            error=error,
        )

        hugging_face_dataset_list_item.additional_properties = d
        return hugging_face_dataset_list_item

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
