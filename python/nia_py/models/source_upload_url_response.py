from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SourceUploadUrlResponse")


@_attrs_define
class SourceUploadUrlResponse:
    """
    Attributes:
        upload_url (str): Signed URL for direct upload (HTTP PUT)
        gcs_path (str): GCS path to pass to create-source payload
        expires_in_seconds (int): Signed URL expiration in seconds
    """

    upload_url: str
    gcs_path: str
    expires_in_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_url = self.upload_url

        gcs_path = self.gcs_path

        expires_in_seconds = self.expires_in_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_url": upload_url,
                "gcs_path": gcs_path,
                "expires_in_seconds": expires_in_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_url = d.pop("upload_url")

        gcs_path = d.pop("gcs_path")

        expires_in_seconds = d.pop("expires_in_seconds")

        source_upload_url_response = cls(
            upload_url=upload_url,
            gcs_path=gcs_path,
            expires_in_seconds=expires_in_seconds,
        )

        source_upload_url_response.additional_properties = d
        return source_upload_url_response

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
