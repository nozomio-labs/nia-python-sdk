from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HuggingFaceDatasetRequest")


@_attrs_define
class HuggingFaceDatasetRequest:
    """Request model for indexing a HuggingFace dataset.

    Attributes:
        url (str): HuggingFace dataset URL (e.g., 'https://huggingface.co/datasets/squad' or 'dair-ai/emotion')
        config (None | str | Unset): Dataset configuration name (for multi-config datasets)
        add_as_global_source (bool | Unset): Add to global shared pool (default: True). Set False for private indexing.
            Default: True.
    """

    url: str
    config: None | str | Unset = UNSET
    add_as_global_source: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        config: None | str | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        else:
            config = self.config

        add_as_global_source = self.add_as_global_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if add_as_global_source is not UNSET:
            field_dict["add_as_global_source"] = add_as_global_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        add_as_global_source = d.pop("add_as_global_source", UNSET)

        hugging_face_dataset_request = cls(
            url=url,
            config=config,
            add_as_global_source=add_as_global_source,
        )

        hugging_face_dataset_request.additional_properties = d
        return hugging_face_dataset_request

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
