from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImageSignedUrlResponse")


@_attrs_define
class ImageSignedUrlResponse:
    """Response containing a signed URL for image download.

    Attributes:
        download_url (str):
        gcs_path (str):
        object_name (str):
        expires_in_seconds (int):
    """

    download_url: str
    gcs_path: str
    object_name: str
    expires_in_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        gcs_path = self.gcs_path

        object_name = self.object_name

        expires_in_seconds = self.expires_in_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "download_url": download_url,
                "gcs_path": gcs_path,
                "object_name": object_name,
                "expires_in_seconds": expires_in_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        download_url = d.pop("download_url")

        gcs_path = d.pop("gcs_path")

        object_name = d.pop("object_name")

        expires_in_seconds = d.pop("expires_in_seconds")

        image_signed_url_response = cls(
            download_url=download_url,
            gcs_path=gcs_path,
            object_name=object_name,
            expires_in_seconds=expires_in_seconds,
        )

        image_signed_url_response.additional_properties = d
        return image_signed_url_response

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
