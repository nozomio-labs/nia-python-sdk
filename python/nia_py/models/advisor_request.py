from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.advisor_request_output_format import AdvisorRequestOutputFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codebase_context import CodebaseContext
    from ..models.search_scope import SearchScope


T = TypeVar("T", bound="AdvisorRequest")


@_attrs_define
class AdvisorRequest:
    """Request model for advisor endpoint.

    Attributes:
        query (str): User's question
        codebase (CodebaseContext): Structured codebase context from the user.
        search_scope (None | SearchScope | Unset): Nia search scope
        output_format (AdvisorRequestOutputFormat | Unset): Output format Default:
            AdvisorRequestOutputFormat.EXPLANATION.
    """

    query: str
    codebase: CodebaseContext
    search_scope: None | SearchScope | Unset = UNSET
    output_format: AdvisorRequestOutputFormat | Unset = AdvisorRequestOutputFormat.EXPLANATION
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_scope import SearchScope

        query = self.query

        codebase = self.codebase.to_dict()

        search_scope: dict[str, Any] | None | Unset
        if isinstance(self.search_scope, Unset):
            search_scope = UNSET
        elif isinstance(self.search_scope, SearchScope):
            search_scope = self.search_scope.to_dict()
        else:
            search_scope = self.search_scope

        output_format: str | Unset = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "codebase": codebase,
            }
        )
        if search_scope is not UNSET:
            field_dict["search_scope"] = search_scope
        if output_format is not UNSET:
            field_dict["output_format"] = output_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.codebase_context import CodebaseContext
        from ..models.search_scope import SearchScope

        d = dict(src_dict)
        query = d.pop("query")

        codebase = CodebaseContext.from_dict(d.pop("codebase"))

        def _parse_search_scope(data: object) -> None | SearchScope | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_scope_type_0 = SearchScope.from_dict(data)

                return search_scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchScope | Unset, data)

        search_scope = _parse_search_scope(d.pop("search_scope", UNSET))

        _output_format = d.pop("output_format", UNSET)
        output_format: AdvisorRequestOutputFormat | Unset
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = AdvisorRequestOutputFormat(_output_format)

        advisor_request = cls(
            query=query,
            codebase=codebase,
            search_scope=search_scope,
            output_format=output_format,
        )

        advisor_request.additional_properties = d
        return advisor_request

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
