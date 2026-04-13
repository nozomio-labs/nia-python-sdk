from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecBody")


@_attrs_define
class ExecBody:
    """
    Attributes:
        command (str): Bash command to execute (e.g. 'cat /file.py', 'grep -rn pattern .')
        cwd (str | Unset): Working directory for relative paths Default: '/'.
    """

    command: str
    cwd: str | Unset = "/"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        cwd = self.cwd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
            }
        )
        if cwd is not UNSET:
            field_dict["cwd"] = cwd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command")

        cwd = d.pop("cwd", UNSET)

        exec_body = cls(
            command=command,
            cwd=cwd,
        )

        exec_body.additional_properties = d
        return exec_body

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
