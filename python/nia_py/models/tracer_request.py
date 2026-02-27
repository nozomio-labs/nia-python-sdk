from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracer_request_mode_type_0 import TracerRequestModeType0
from ..models.tracer_request_model_type_0 import TracerRequestModelType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="TracerRequest")


@_attrs_define
class TracerRequest:
    """
    Attributes:
        query (str): Research question
        repositories (list[str] | None | Unset): Repositories in owner/repo format
        context (None | str | Unset): Additional context
        model (None | TracerRequestModelType0 | Unset): Optional model override (claude-haiku-4-5-20251001, claude-
            opus-4-6, or claude-opus-4-6-1m). Must match mode when both are provided.
        mode (None | TracerRequestModeType0 | Unset): Tracer mode: tracer-fast (Haiku) or tracer-deep (Opus). Defaults
            to tracer-deep. When mode and model are both provided, they must agree.
    """

    query: str
    repositories: list[str] | None | Unset = UNSET
    context: None | str | Unset = UNSET
    model: None | TracerRequestModelType0 | Unset = UNSET
    mode: None | TracerRequestModeType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        repositories: list[str] | None | Unset
        if isinstance(self.repositories, Unset):
            repositories = UNSET
        elif isinstance(self.repositories, list):
            repositories = self.repositories

        else:
            repositories = self.repositories

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, TracerRequestModelType0):
            model = self.model.value
        else:
            model = self.model

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, TracerRequestModeType0):
            mode = self.mode.value
        else:
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if context is not UNSET:
            field_dict["context"] = context
        if model is not UNSET:
            field_dict["model"] = model
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_repositories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repositories_type_0 = cast(list[str], data)

                return repositories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        repositories = _parse_repositories(d.pop("repositories", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        def _parse_model(data: object) -> None | TracerRequestModelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_0 = TracerRequestModelType0(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TracerRequestModelType0 | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_mode(data: object) -> None | TracerRequestModeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = TracerRequestModeType0(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TracerRequestModeType0 | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        tracer_request = cls(
            query=query,
            repositories=repositories,
            context=context,
            model=model,
            mode=mode,
        )

        tracer_request.additional_properties = d
        return tracer_request

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
