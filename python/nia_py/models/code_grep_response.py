from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_grep_options import CodeGrepOptions
    from ..models.code_grep_response_counts_type_0 import CodeGrepResponseCountsType0
    from ..models.code_grep_response_matches_type_0 import CodeGrepResponseMatchesType0
    from ..models.code_grep_response_matches_type_1_item import CodeGrepResponseMatchesType1Item
    from ..models.grep_file_result import GrepFileResult


T = TypeVar("T", bound="CodeGrepResponse")


@_attrs_define
class CodeGrepResponse:
    """Response for code grep search.

    Attributes:
        pattern (str): The search pattern used
        success (bool | Unset): Whether the search succeeded Default: True.
        path_filter (str | Unset): Path filter applied Default: '/'.
        total_matches (int | Unset): Total number of matches found Default: 0.
        files_searched (int | Unset): Number of files searched Default: 0.
        files_with_matches (int | Unset): Number of files with matches Default: 0.
        truncated (bool | Unset): Whether results were truncated Default: False.
        options (CodeGrepOptions | Unset): Options used for code grep search.
        matches (CodeGrepResponseMatchesType0 | list[CodeGrepResponseMatchesType1Item] | None | Unset): Matches (content
            mode)
        files (list[str] | None | Unset): Files with matches (files_with_matches mode)
        counts (CodeGrepResponseCountsType0 | None | Unset): Match counts per file (count mode)
        results (list[GrepFileResult] | None | Unset): Grep results by file (deprecated)
    """

    pattern: str
    success: bool | Unset = True
    path_filter: str | Unset = "/"
    total_matches: int | Unset = 0
    files_searched: int | Unset = 0
    files_with_matches: int | Unset = 0
    truncated: bool | Unset = False
    options: CodeGrepOptions | Unset = UNSET
    matches: CodeGrepResponseMatchesType0 | list[CodeGrepResponseMatchesType1Item] | None | Unset = UNSET
    files: list[str] | None | Unset = UNSET
    counts: CodeGrepResponseCountsType0 | None | Unset = UNSET
    results: list[GrepFileResult] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.code_grep_response_counts_type_0 import CodeGrepResponseCountsType0
        from ..models.code_grep_response_matches_type_0 import CodeGrepResponseMatchesType0

        pattern = self.pattern

        success = self.success

        path_filter = self.path_filter

        total_matches = self.total_matches

        files_searched = self.files_searched

        files_with_matches = self.files_with_matches

        truncated = self.truncated

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        matches: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.matches, Unset):
            matches = UNSET
        elif isinstance(self.matches, CodeGrepResponseMatchesType0):
            matches = self.matches.to_dict()
        elif isinstance(self.matches, list):
            matches = []
            for matches_type_1_item_data in self.matches:
                matches_type_1_item = matches_type_1_item_data.to_dict()
                matches.append(matches_type_1_item)

        else:
            matches = self.matches

        files: list[str] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = self.files

        else:
            files = self.files

        counts: dict[str, Any] | None | Unset
        if isinstance(self.counts, Unset):
            counts = UNSET
        elif isinstance(self.counts, CodeGrepResponseCountsType0):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success
        if path_filter is not UNSET:
            field_dict["path_filter"] = path_filter
        if total_matches is not UNSET:
            field_dict["total_matches"] = total_matches
        if files_searched is not UNSET:
            field_dict["files_searched"] = files_searched
        if files_with_matches is not UNSET:
            field_dict["files_with_matches"] = files_with_matches
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if options is not UNSET:
            field_dict["options"] = options
        if matches is not UNSET:
            field_dict["matches"] = matches
        if files is not UNSET:
            field_dict["files"] = files
        if counts is not UNSET:
            field_dict["counts"] = counts
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_grep_options import CodeGrepOptions
        from ..models.code_grep_response_counts_type_0 import CodeGrepResponseCountsType0
        from ..models.code_grep_response_matches_type_0 import CodeGrepResponseMatchesType0
        from ..models.code_grep_response_matches_type_1_item import CodeGrepResponseMatchesType1Item
        from ..models.grep_file_result import GrepFileResult

        d = dict(src_dict)
        pattern = d.pop("pattern")

        success = d.pop("success", UNSET)

        path_filter = d.pop("path_filter", UNSET)

        total_matches = d.pop("total_matches", UNSET)

        files_searched = d.pop("files_searched", UNSET)

        files_with_matches = d.pop("files_with_matches", UNSET)

        truncated = d.pop("truncated", UNSET)

        _options = d.pop("options", UNSET)
        options: CodeGrepOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = CodeGrepOptions.from_dict(_options)

        def _parse_matches(
            data: object,
        ) -> CodeGrepResponseMatchesType0 | list[CodeGrepResponseMatchesType1Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                matches_type_0 = CodeGrepResponseMatchesType0.from_dict(data)

                return matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matches_type_1 = []
                _matches_type_1 = data
                for matches_type_1_item_data in _matches_type_1:
                    matches_type_1_item = CodeGrepResponseMatchesType1Item.from_dict(matches_type_1_item_data)

                    matches_type_1.append(matches_type_1_item)

                return matches_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CodeGrepResponseMatchesType0 | list[CodeGrepResponseMatchesType1Item] | None | Unset, data)

        matches = _parse_matches(d.pop("matches", UNSET))

        def _parse_files(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = cast(list[str], data)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_counts(data: object) -> CodeGrepResponseCountsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counts_type_0 = CodeGrepResponseCountsType0.from_dict(data)

                return counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CodeGrepResponseCountsType0 | None | Unset, data)

        counts = _parse_counts(d.pop("counts", UNSET))

        def _parse_results(data: object) -> list[GrepFileResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = GrepFileResult.from_dict(results_type_0_item_data)

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GrepFileResult] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))

        code_grep_response = cls(
            pattern=pattern,
            success=success,
            path_filter=path_filter,
            total_matches=total_matches,
            files_searched=files_searched,
            files_with_matches=files_with_matches,
            truncated=truncated,
            options=options,
            matches=matches,
            files=files,
            counts=counts,
            results=results,
        )

        code_grep_response.additional_properties = d
        return code_grep_response

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
