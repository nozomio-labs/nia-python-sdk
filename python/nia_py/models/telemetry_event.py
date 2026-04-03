from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryEvent")


@_attrs_define
class TelemetryEvent:
    """
    Attributes:
        seq (int):
        ts (str):
        raw (str):
        name (str):
        type_ (str | Unset):  Default: 'command'.
        args (list[Any] | Unset):
        cwd (str | Unset):  Default: ''.
        exit_code (int | Unset):  Default: 0.
        stdout_bytes (int | Unset):  Default: 0.
        stderr_bytes (int | Unset):  Default: 0.
        duration_ms (int | Unset):  Default: 0.
        pattern (None | str | Unset):
        paths (list[Any] | None | Unset):
        flags (list[Any] | None | Unset):
        result_files (list[Any] | None | Unset):
    """

    seq: int
    ts: str
    raw: str
    name: str
    type_: str | Unset = "command"
    args: list[Any] | Unset = UNSET
    cwd: str | Unset = ""
    exit_code: int | Unset = 0
    stdout_bytes: int | Unset = 0
    stderr_bytes: int | Unset = 0
    duration_ms: int | Unset = 0
    pattern: None | str | Unset = UNSET
    paths: list[Any] | None | Unset = UNSET
    flags: list[Any] | None | Unset = UNSET
    result_files: list[Any] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        ts = self.ts

        raw = self.raw

        name = self.name

        type_ = self.type_

        args: list[Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        cwd = self.cwd

        exit_code = self.exit_code

        stdout_bytes = self.stdout_bytes

        stderr_bytes = self.stderr_bytes

        duration_ms = self.duration_ms

        pattern: None | str | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        else:
            pattern = self.pattern

        paths: list[Any] | None | Unset
        if isinstance(self.paths, Unset):
            paths = UNSET
        elif isinstance(self.paths, list):
            paths = self.paths

        else:
            paths = self.paths

        flags: list[Any] | None | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        elif isinstance(self.flags, list):
            flags = self.flags

        else:
            flags = self.flags

        result_files: list[Any] | None | Unset
        if isinstance(self.result_files, Unset):
            result_files = UNSET
        elif isinstance(self.result_files, list):
            result_files = self.result_files

        else:
            result_files = self.result_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seq": seq,
                "ts": ts,
                "raw": raw,
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if args is not UNSET:
            field_dict["args"] = args
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if stdout_bytes is not UNSET:
            field_dict["stdout_bytes"] = stdout_bytes
        if stderr_bytes is not UNSET:
            field_dict["stderr_bytes"] = stderr_bytes
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if paths is not UNSET:
            field_dict["paths"] = paths
        if flags is not UNSET:
            field_dict["flags"] = flags
        if result_files is not UNSET:
            field_dict["result_files"] = result_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq")

        ts = d.pop("ts")

        raw = d.pop("raw")

        name = d.pop("name")

        type_ = d.pop("type", UNSET)

        args = cast(list[Any], d.pop("args", UNSET))

        cwd = d.pop("cwd", UNSET)

        exit_code = d.pop("exit_code", UNSET)

        stdout_bytes = d.pop("stdout_bytes", UNSET)

        stderr_bytes = d.pop("stderr_bytes", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        def _parse_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))

        def _parse_paths(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                paths_type_0 = cast(list[Any], data)

                return paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        paths = _parse_paths(d.pop("paths", UNSET))

        def _parse_flags(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                flags_type_0 = cast(list[Any], data)

                return flags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))

        def _parse_result_files(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_files_type_0 = cast(list[Any], data)

                return result_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        result_files = _parse_result_files(d.pop("result_files", UNSET))

        telemetry_event = cls(
            seq=seq,
            ts=ts,
            raw=raw,
            name=name,
            type_=type_,
            args=args,
            cwd=cwd,
            exit_code=exit_code,
            stdout_bytes=stdout_bytes,
            stderr_bytes=stderr_bytes,
            duration_ms=duration_ms,
            pattern=pattern,
            paths=paths,
            flags=flags,
            result_files=result_files,
        )

        telemetry_event.additional_properties = d
        return telemetry_event

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
