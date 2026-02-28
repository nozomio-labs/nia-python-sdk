from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignupResponse")


@_attrs_define
class SignupResponse:
    """
    Attributes:
        user_id (str):
        organization_id (str):
        bootstrap_token (str): One-time token to exchange for an API key via /v2/auth/bootstrap-key
        expires_at (str):
        email_verified (bool | Unset): Whether the email is already verified in the identity provider Default: False.
    """

    user_id: str
    organization_id: str
    bootstrap_token: str
    expires_at: str
    email_verified: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        organization_id = self.organization_id

        bootstrap_token = self.bootstrap_token

        expires_at = self.expires_at

        email_verified = self.email_verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "organization_id": organization_id,
                "bootstrap_token": bootstrap_token,
                "expires_at": expires_at,
            }
        )
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        organization_id = d.pop("organization_id")

        bootstrap_token = d.pop("bootstrap_token")

        expires_at = d.pop("expires_at")

        email_verified = d.pop("email_verified", UNSET)

        signup_response = cls(
            user_id=user_id,
            organization_id=organization_id,
            bootstrap_token=bootstrap_token,
            expires_at=expires_at,
            email_verified=email_verified,
        )

        signup_response.additional_properties = d
        return signup_response

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
