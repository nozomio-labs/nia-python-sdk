from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_tree_response_tree import DocTreeResponseTree


T = TypeVar("T", bound="DocTreeResponse")


@_attrs_define
class DocTreeResponse:
    """Response for documentation tree.

    Attributes:
        success (bool | Unset): Whether the request succeeded Default: True.
        tree (DocTreeResponseTree | Unset): Nested tree structure (keys are path segments, values are URLs or nested
            dicts)
        tree_string (None | str | Unset): Human-readable tree representation
        tree_type (None | str | Unset): Tree type: url_tree, document_tree, or huggingface_dataset
        base_url (None | str | Unset): Base URL of the documentation
        page_count (int | Unset): Total number of pages Default: 0.
        message (None | str | Unset): Status message
        dataset_id (None | str | Unset): HuggingFace dataset ID
        owner (None | str | Unset): Dataset owner
        description (None | str | Unset): Dataset description
        splits (list[str] | None | Unset): Available splits (train, test, validation)
        columns (list[Any] | None | Unset): Dataset columns with name and type
        row_count (int | None | Unset): Total rows in dataset
        indexed_row_count (int | None | Unset): Number of rows indexed
        sampling_strategy (None | str | Unset): Sampling strategy used for indexing
    """

    success: bool | Unset = True
    tree: DocTreeResponseTree | Unset = UNSET
    tree_string: None | str | Unset = UNSET
    tree_type: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    page_count: int | Unset = 0
    message: None | str | Unset = UNSET
    dataset_id: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    splits: list[str] | None | Unset = UNSET
    columns: list[Any] | None | Unset = UNSET
    row_count: int | None | Unset = UNSET
    indexed_row_count: int | None | Unset = UNSET
    sampling_strategy: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        tree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tree, Unset):
            tree = self.tree.to_dict()

        tree_string: None | str | Unset
        if isinstance(self.tree_string, Unset):
            tree_string = UNSET
        else:
            tree_string = self.tree_string

        tree_type: None | str | Unset
        if isinstance(self.tree_type, Unset):
            tree_type = UNSET
        else:
            tree_type = self.tree_type

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        page_count = self.page_count

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        dataset_id: None | str | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = self.dataset_id

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

        columns: list[Any] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = self.columns

        else:
            columns = self.columns

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if tree is not UNSET:
            field_dict["tree"] = tree
        if tree_string is not UNSET:
            field_dict["tree_string"] = tree_string
        if tree_type is not UNSET:
            field_dict["tree_type"] = tree_type
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if message is not UNSET:
            field_dict["message"] = message
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
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
        if sampling_strategy is not UNSET:
            field_dict["sampling_strategy"] = sampling_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.doc_tree_response_tree import DocTreeResponseTree

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _tree = d.pop("tree", UNSET)
        tree: DocTreeResponseTree | Unset
        if isinstance(_tree, Unset):
            tree = UNSET
        else:
            tree = DocTreeResponseTree.from_dict(_tree)

        def _parse_tree_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_string = _parse_tree_string(d.pop("tree_string", UNSET))

        def _parse_tree_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_type = _parse_tree_type(d.pop("tree_type", UNSET))

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))

        page_count = d.pop("page_count", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_dataset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_id = _parse_dataset_id(d.pop("dataset_id", UNSET))

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

        def _parse_columns(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = cast(list[Any], data)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))

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

        doc_tree_response = cls(
            success=success,
            tree=tree,
            tree_string=tree_string,
            tree_type=tree_type,
            base_url=base_url,
            page_count=page_count,
            message=message,
            dataset_id=dataset_id,
            owner=owner,
            description=description,
            splits=splits,
            columns=columns,
            row_count=row_count,
            indexed_row_count=indexed_row_count,
            sampling_strategy=sampling_strategy,
        )

        doc_tree_response.additional_properties = d
        return doc_tree_response

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
