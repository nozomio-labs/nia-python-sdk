from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hugging_face_dataset_response_columns_item import HuggingFaceDatasetResponseColumnsItem


T = TypeVar("T", bound="HuggingFaceDatasetResponse")


@_attrs_define
class HuggingFaceDatasetResponse:
    """Response model for HuggingFace dataset indexing.

    Attributes:
        id (str):
        dataset_id (str):
        url (str):
        status (str):
        created_at (str):
        updated_at (str):
        owner (None | str | Unset):
        description (None | str | Unset):
        splits (list[str] | Unset):
        columns (list[HuggingFaceDatasetResponseColumnsItem] | Unset):
        row_count (int | Unset):  Default: 0.
        indexed_row_count (int | Unset):  Default: 0.
        chunk_count (int | Unset):  Default: 0.
        sampling_strategy (None | str | Unset):
        license_ (None | str | Unset):
        error (None | str | Unset):
    """

    id: str
    dataset_id: str
    url: str
    status: str
    created_at: str
    updated_at: str
    owner: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    splits: list[str] | Unset = UNSET
    columns: list[HuggingFaceDatasetResponseColumnsItem] | Unset = UNSET
    row_count: int | Unset = 0
    indexed_row_count: int | Unset = 0
    chunk_count: int | Unset = 0
    sampling_strategy: None | str | Unset = UNSET
    license_: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dataset_id = self.dataset_id

        url = self.url

        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

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

        splits: list[str] | Unset = UNSET
        if not isinstance(self.splits, Unset):
            splits = self.splits

        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        row_count = self.row_count

        indexed_row_count = self.indexed_row_count

        chunk_count = self.chunk_count

        sampling_strategy: None | str | Unset
        if isinstance(self.sampling_strategy, Unset):
            sampling_strategy = UNSET
        else:
            sampling_strategy = self.sampling_strategy

        license_: None | str | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        else:
            license_ = self.license_

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
                "dataset_id": dataset_id,
                "url": url,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if description is not UNSET:
            field_dict["description"] = description
        if splits is not UNSET:
            field_dict["splits"] = splits
        if columns is not UNSET:
            field_dict["columns"] = columns
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if indexed_row_count is not UNSET:
            field_dict["indexed_row_count"] = indexed_row_count
        if chunk_count is not UNSET:
            field_dict["chunk_count"] = chunk_count
        if sampling_strategy is not UNSET:
            field_dict["sampling_strategy"] = sampling_strategy
        if license_ is not UNSET:
            field_dict["license"] = license_
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hugging_face_dataset_response_columns_item import HuggingFaceDatasetResponseColumnsItem

        d = dict(src_dict)
        id = d.pop("id")

        dataset_id = d.pop("dataset_id")

        url = d.pop("url")

        status = d.pop("status")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

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

        splits = cast(list[str], d.pop("splits", UNSET))

        _columns = d.pop("columns", UNSET)
        columns: list[HuggingFaceDatasetResponseColumnsItem] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = HuggingFaceDatasetResponseColumnsItem.from_dict(columns_item_data)

                columns.append(columns_item)

        row_count = d.pop("row_count", UNSET)

        indexed_row_count = d.pop("indexed_row_count", UNSET)

        chunk_count = d.pop("chunk_count", UNSET)

        def _parse_sampling_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sampling_strategy = _parse_sampling_strategy(d.pop("sampling_strategy", UNSET))

        def _parse_license_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        hugging_face_dataset_response = cls(
            id=id,
            dataset_id=dataset_id,
            url=url,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            owner=owner,
            description=description,
            splits=splits,
            columns=columns,
            row_count=row_count,
            indexed_row_count=indexed_row_count,
            chunk_count=chunk_count,
            sampling_strategy=sampling_strategy,
            license_=license_,
            error=error,
        )

        hugging_face_dataset_response.additional_properties = d
        return hugging_face_dataset_response

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
