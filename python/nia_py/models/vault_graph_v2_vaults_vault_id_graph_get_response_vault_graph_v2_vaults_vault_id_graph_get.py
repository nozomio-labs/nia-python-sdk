from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet")


@_attrs_define
class VaultGraphV2VaultsVaultIdGraphGetResponseVaultGraphV2VaultsVaultIdGraphGet:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vault_graph_v2_vaults_vault_id_graph_get_response_vault_graph_v2_vaults_vault_id_graph_get = cls()

        vault_graph_v2_vaults_vault_id_graph_get_response_vault_graph_v2_vaults_vault_id_graph_get.additional_properties = d
        return vault_graph_v2_vaults_vault_id_graph_get_response_vault_graph_v2_vaults_vault_id_graph_get

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
