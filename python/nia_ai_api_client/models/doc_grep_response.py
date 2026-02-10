from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_grep_file_match import DocGrepFileMatch
    from ..models.doc_grep_options import DocGrepOptions
    from ..models.doc_grep_response_counts_type_0 import DocGrepResponseCountsType0
    from ..models.hugging_face_grep_match import HuggingFaceGrepMatch


T = TypeVar("T", bound="DocGrepResponse")


@_attrs_define
class DocGrepResponse:
    """Response for documentation grep.

    Attributes:
        pattern (str): Search pattern used
        success (bool | Unset): Whether the search succeeded Default: True.
        path_filter (str | Unset): Path filter applied Default: '/'.
        total_matches (int | Unset): Total number of matches Default: 0.
        files_searched (int | Unset): Number of files searched Default: 0.
        files_with_matches (int | Unset): Number of files with matches Default: 0.
        truncated (bool | Unset): Whether results were truncated Default: False.
        options (DocGrepOptions | Unset): Options used for grep search.
        matches (list[DocGrepFileMatch] | list[HuggingFaceGrepMatch] | None | Unset): Matches (format depends on source
            type)
        files (list[str] | None | Unset): Files with matches (files_with_matches mode)
        counts (DocGrepResponseCountsType0 | None | Unset): Match counts per file (count mode)
        source_type (None | str | Unset): Source type (huggingface_dataset, documentation, etc.)
    """

    pattern: str
    success: bool | Unset = True
    path_filter: str | Unset = "/"
    total_matches: int | Unset = 0
    files_searched: int | Unset = 0
    files_with_matches: int | Unset = 0
    truncated: bool | Unset = False
    options: DocGrepOptions | Unset = UNSET
    matches: list[DocGrepFileMatch] | list[HuggingFaceGrepMatch] | None | Unset = UNSET
    files: list[str] | None | Unset = UNSET
    counts: DocGrepResponseCountsType0 | None | Unset = UNSET
    source_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.doc_grep_response_counts_type_0 import DocGrepResponseCountsType0

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

        matches: list[dict[str, Any]] | None | Unset
        if isinstance(self.matches, Unset):
            matches = UNSET
        elif isinstance(self.matches, list):
            matches = []
            for matches_type_0_item_data in self.matches:
                matches_type_0_item = matches_type_0_item_data.to_dict()
                matches.append(matches_type_0_item)

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
        elif isinstance(self.counts, DocGrepResponseCountsType0):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

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
        if source_type is not UNSET:
            field_dict["source_type"] = source_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.doc_grep_file_match import DocGrepFileMatch
        from ..models.doc_grep_options import DocGrepOptions
        from ..models.doc_grep_response_counts_type_0 import DocGrepResponseCountsType0
        from ..models.hugging_face_grep_match import HuggingFaceGrepMatch

        d = dict(src_dict)
        pattern = d.pop("pattern")

        success = d.pop("success", UNSET)

        path_filter = d.pop("path_filter", UNSET)

        total_matches = d.pop("total_matches", UNSET)

        files_searched = d.pop("files_searched", UNSET)

        files_with_matches = d.pop("files_with_matches", UNSET)

        truncated = d.pop("truncated", UNSET)

        _options = d.pop("options", UNSET)
        options: DocGrepOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = DocGrepOptions.from_dict(_options)

        def _parse_matches(data: object) -> list[DocGrepFileMatch] | list[HuggingFaceGrepMatch] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matches_type_0 = []
                _matches_type_0 = data
                for matches_type_0_item_data in _matches_type_0:
                    matches_type_0_item = HuggingFaceGrepMatch.from_dict(matches_type_0_item_data)

                    matches_type_0.append(matches_type_0_item)

                return matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matches_type_1 = []
                _matches_type_1 = data
                for matches_type_1_item_data in _matches_type_1:
                    matches_type_1_item = DocGrepFileMatch.from_dict(matches_type_1_item_data)

                    matches_type_1.append(matches_type_1_item)

                return matches_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DocGrepFileMatch] | list[HuggingFaceGrepMatch] | None | Unset, data)

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

        def _parse_counts(data: object) -> DocGrepResponseCountsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counts_type_0 = DocGrepResponseCountsType0.from_dict(data)

                return counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocGrepResponseCountsType0 | None | Unset, data)

        counts = _parse_counts(d.pop("counts", UNSET))

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        doc_grep_response = cls(
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
            source_type=source_type,
        )

        doc_grep_response.additional_properties = d
        return doc_grep_response

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
