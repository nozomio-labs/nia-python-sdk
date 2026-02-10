from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codebase_context_dependencies_type_0 import CodebaseContextDependenciesType0
    from ..models.codebase_context_files import CodebaseContextFiles


T = TypeVar("T", bound="CodebaseContext")


@_attrs_define
class CodebaseContext:
    """Structured codebase context from the user.

    Attributes:
        files (CodebaseContextFiles | Unset): Map of file_path -> file_content
        file_tree (None | str | Unset): Directory structure (from tree command or similar)
        dependencies (CodebaseContextDependenciesType0 | None | Unset): Dependency files: package.json,
            requirements.txt, etc.
        git_diff (None | str | Unset): Git diff for migration/upgrade scenarios
        summary (None | str | Unset): High-level description of the codebase
        focus_paths (list[str] | None | Unset): Paths to prioritize in analysis
    """

    files: CodebaseContextFiles | Unset = UNSET
    file_tree: None | str | Unset = UNSET
    dependencies: CodebaseContextDependenciesType0 | None | Unset = UNSET
    git_diff: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    focus_paths: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.codebase_context_dependencies_type_0 import CodebaseContextDependenciesType0

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        file_tree: None | str | Unset
        if isinstance(self.file_tree, Unset):
            file_tree = UNSET
        else:
            file_tree = self.file_tree

        dependencies: dict[str, Any] | None | Unset
        if isinstance(self.dependencies, Unset):
            dependencies = UNSET
        elif isinstance(self.dependencies, CodebaseContextDependenciesType0):
            dependencies = self.dependencies.to_dict()
        else:
            dependencies = self.dependencies

        git_diff: None | str | Unset
        if isinstance(self.git_diff, Unset):
            git_diff = UNSET
        else:
            git_diff = self.git_diff

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        focus_paths: list[str] | None | Unset
        if isinstance(self.focus_paths, Unset):
            focus_paths = UNSET
        elif isinstance(self.focus_paths, list):
            focus_paths = self.focus_paths

        else:
            focus_paths = self.focus_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if file_tree is not UNSET:
            field_dict["file_tree"] = file_tree
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if git_diff is not UNSET:
            field_dict["git_diff"] = git_diff
        if summary is not UNSET:
            field_dict["summary"] = summary
        if focus_paths is not UNSET:
            field_dict["focus_paths"] = focus_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.codebase_context_dependencies_type_0 import CodebaseContextDependenciesType0
        from ..models.codebase_context_files import CodebaseContextFiles

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: CodebaseContextFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = CodebaseContextFiles.from_dict(_files)

        def _parse_file_tree(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_tree = _parse_file_tree(d.pop("file_tree", UNSET))

        def _parse_dependencies(data: object) -> CodebaseContextDependenciesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dependencies_type_0 = CodebaseContextDependenciesType0.from_dict(data)

                return dependencies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CodebaseContextDependenciesType0 | None | Unset, data)

        dependencies = _parse_dependencies(d.pop("dependencies", UNSET))

        def _parse_git_diff(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        git_diff = _parse_git_diff(d.pop("git_diff", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_focus_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                focus_paths_type_0 = cast(list[str], data)

                return focus_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        focus_paths = _parse_focus_paths(d.pop("focus_paths", UNSET))

        codebase_context = cls(
            files=files,
            file_tree=file_tree,
            dependencies=dependencies,
            git_diff=git_diff,
            summary=summary,
            focus_paths=focus_paths,
        )

        codebase_context.additional_properties = d
        return codebase_context

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
