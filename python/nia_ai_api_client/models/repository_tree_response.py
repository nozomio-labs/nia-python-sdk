from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_tree_stats import RepositoryTreeStats
    from ..models.tree_item import TreeItem


T = TypeVar("T", bound="RepositoryTreeResponse")


@_attrs_define
class RepositoryTreeResponse:
    """Response for repository tree endpoints.

    Attributes:
        repository_id (None | str | Unset): Repository identifier
        owner (None | str | Unset): Repository owner
        repo (None | str | Unset): Repository name
        branch (None | str | Unset): Branch name
        sha (None | str | Unset): Tree SHA
        tree_text (None | str | Unset): Human-readable tree structure
        stats (None | RepositoryTreeStats | Unset): Tree statistics
        files (list[TreeItem] | Unset): File tree items
        directories (list[TreeItem] | Unset): Directory tree items
        truncated (bool | Unset): Whether the tree was truncated Default: False.
        source (None | str | Unset): Source of the tree data
        retrieved_at (None | str | Unset): Timestamp when tree was retrieved
        tree (list[TreeItem] | None | Unset): Tree items (deprecated)
        formatted_tree (None | str | Unset): Formatted tree (deprecated, use tree_text)
        total_items (int | None | Unset): Total items (deprecated, use stats.total_items)
        max_depth (int | None | Unset): Max depth (deprecated, use stats.max_depth)
    """

    repository_id: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    repo: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    sha: None | str | Unset = UNSET
    tree_text: None | str | Unset = UNSET
    stats: None | RepositoryTreeStats | Unset = UNSET
    files: list[TreeItem] | Unset = UNSET
    directories: list[TreeItem] | Unset = UNSET
    truncated: bool | Unset = False
    source: None | str | Unset = UNSET
    retrieved_at: None | str | Unset = UNSET
    tree: list[TreeItem] | None | Unset = UNSET
    formatted_tree: None | str | Unset = UNSET
    total_items: int | None | Unset = UNSET
    max_depth: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.repository_tree_stats import RepositoryTreeStats

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = self.repository_id

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        repo: None | str | Unset
        if isinstance(self.repo, Unset):
            repo = UNSET
        else:
            repo = self.repo

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        sha: None | str | Unset
        if isinstance(self.sha, Unset):
            sha = UNSET
        else:
            sha = self.sha

        tree_text: None | str | Unset
        if isinstance(self.tree_text, Unset):
            tree_text = UNSET
        else:
            tree_text = self.tree_text

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, RepositoryTreeStats):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        directories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.directories, Unset):
            directories = []
            for directories_item_data in self.directories:
                directories_item = directories_item_data.to_dict()
                directories.append(directories_item)

        truncated = self.truncated

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        retrieved_at: None | str | Unset
        if isinstance(self.retrieved_at, Unset):
            retrieved_at = UNSET
        else:
            retrieved_at = self.retrieved_at

        tree: list[dict[str, Any]] | None | Unset
        if isinstance(self.tree, Unset):
            tree = UNSET
        elif isinstance(self.tree, list):
            tree = []
            for tree_type_0_item_data in self.tree:
                tree_type_0_item = tree_type_0_item_data.to_dict()
                tree.append(tree_type_0_item)

        else:
            tree = self.tree

        formatted_tree: None | str | Unset
        if isinstance(self.formatted_tree, Unset):
            formatted_tree = UNSET
        else:
            formatted_tree = self.formatted_tree

        total_items: int | None | Unset
        if isinstance(self.total_items, Unset):
            total_items = UNSET
        else:
            total_items = self.total_items

        max_depth: int | None | Unset
        if isinstance(self.max_depth, Unset):
            max_depth = UNSET
        else:
            max_depth = self.max_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if repo is not UNSET:
            field_dict["repo"] = repo
        if branch is not UNSET:
            field_dict["branch"] = branch
        if sha is not UNSET:
            field_dict["sha"] = sha
        if tree_text is not UNSET:
            field_dict["tree_text"] = tree_text
        if stats is not UNSET:
            field_dict["stats"] = stats
        if files is not UNSET:
            field_dict["files"] = files
        if directories is not UNSET:
            field_dict["directories"] = directories
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if source is not UNSET:
            field_dict["source"] = source
        if retrieved_at is not UNSET:
            field_dict["retrieved_at"] = retrieved_at
        if tree is not UNSET:
            field_dict["tree"] = tree
        if formatted_tree is not UNSET:
            field_dict["formatted_tree"] = formatted_tree
        if total_items is not UNSET:
            field_dict["total_items"] = total_items
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_tree_stats import RepositoryTreeStats
        from ..models.tree_item import TreeItem

        d = dict(src_dict)

        def _parse_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_id = _parse_repository_id(d.pop("repository_id", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_repo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repo = _parse_repo(d.pop("repo", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_sha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sha = _parse_sha(d.pop("sha", UNSET))

        def _parse_tree_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_text = _parse_tree_text(d.pop("tree_text", UNSET))

        def _parse_stats(data: object) -> None | RepositoryTreeStats | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = RepositoryTreeStats.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RepositoryTreeStats | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        _files = d.pop("files", UNSET)
        files: list[TreeItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = TreeItem.from_dict(files_item_data)

                files.append(files_item)

        _directories = d.pop("directories", UNSET)
        directories: list[TreeItem] | Unset = UNSET
        if _directories is not UNSET:
            directories = []
            for directories_item_data in _directories:
                directories_item = TreeItem.from_dict(directories_item_data)

                directories.append(directories_item)

        truncated = d.pop("truncated", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_retrieved_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retrieved_at = _parse_retrieved_at(d.pop("retrieved_at", UNSET))

        def _parse_tree(data: object) -> list[TreeItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tree_type_0 = []
                _tree_type_0 = data
                for tree_type_0_item_data in _tree_type_0:
                    tree_type_0_item = TreeItem.from_dict(tree_type_0_item_data)

                    tree_type_0.append(tree_type_0_item)

                return tree_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TreeItem] | None | Unset, data)

        tree = _parse_tree(d.pop("tree", UNSET))

        def _parse_formatted_tree(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted_tree = _parse_formatted_tree(d.pop("formatted_tree", UNSET))

        def _parse_total_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_items = _parse_total_items(d.pop("total_items", UNSET))

        def _parse_max_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_depth = _parse_max_depth(d.pop("max_depth", UNSET))

        repository_tree_response = cls(
            repository_id=repository_id,
            owner=owner,
            repo=repo,
            branch=branch,
            sha=sha,
            tree_text=tree_text,
            stats=stats,
            files=files,
            directories=directories,
            truncated=truncated,
            source=source,
            retrieved_at=retrieved_at,
            tree=tree,
            formatted_tree=formatted_tree,
            total_items=total_items,
            max_depth=max_depth,
        )

        repository_tree_response.additional_properties = d
        return repository_tree_response

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
