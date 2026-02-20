from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_source_filters import LocalSourceFilters
    from ..models.query_search_request_data_sources_item_type_1 import QuerySearchRequestDataSourcesItemType1
    from ..models.query_search_request_local_folders_item_type_1 import QuerySearchRequestLocalFoldersItemType1
    from ..models.query_search_request_messages_item import QuerySearchRequestMessagesItem
    from ..models.query_search_request_repositories_item_type_1 import QuerySearchRequestRepositoriesItemType1
    from ..models.slack_search_filters import SlackSearchFilters


T = TypeVar("T", bound="QuerySearchRequest")


@_attrs_define
class QuerySearchRequest:
    """
    Attributes:
        messages (list[QuerySearchRequestMessagesItem]): List of chat messages
        repositories (list[QuerySearchRequestRepositoriesItemType1 | str] | Unset): List of repositories to query. Can
            be strings (slug, display name) or dicts with a 'repository' field.
        data_sources (list[QuerySearchRequestDataSourcesItemType1 | str] | Unset): List of data sources to query. Can be
            strings (display_name, URL, or source_id) or dicts with 'source_id' or 'identifier' fields
        local_folders (list[QuerySearchRequestLocalFoldersItemType1 | str] | Unset): List of local folders to query. Can
            be strings (display_name or local_folder_id) or dicts with 'local_folder_id' or 'identifier' fields. Local
            folders are private and user-scoped.
        slack_workspaces (list[str] | Unset): List of Slack installation IDs to include in search
        slack_filters (None | SlackSearchFilters | Unset): Filters for Slack message results (channels, users, date
            range)
        category (None | str | Unset): Filter local folder results by classification category (e.g., 'Work', 'Personal')
        local_source_filters (LocalSourceFilters | None | Unset): Filters for local/personal sources (messages,
            contacts, etc.)
        search_mode (str | Unset): Search mode: 'repositories', 'sources', or 'unified' Default: 'unified'.
        stream (bool | Unset): Whether to stream the response Default: False.
        include_sources (bool | Unset): Whether to include source texts in the response Default: True.
        fast_mode (bool | Unset): Skip LLM processing for faster results (100-500ms vs 2-8s). Set to false for deeper
            analysis. Default: True.
        skip_llm (bool | Unset): Return raw search results without any LLM processing. Returns only sources with scores.
            Default: False.
        reasoning_strategy (str | Unset): Retrieval strategy: 'vector' (default similarity search), 'tree' (LLM-guided
            tree navigation for PDFs), or 'hybrid' (both combined) Default: 'vector'.
        max_tokens (int | None | Unset): Maximum tokens in response. Results truncated when budget reached.
        model (None | str | Unset): Synthesis model override. Allowed: claude-sonnet-4-5, gpt-5.2-2025-12-11, claude-
            haiku-4-5-20251001
        semantic_cache_threshold (float | Unset): Minimum similarity for semantic cache hit (non-streaming only)
            Default: 0.92.
        bypass_semantic_cache (bool | Unset): Skip semantic cache (L2) lookup Default: False.
        include_follow_ups (bool | Unset): Generate follow-up questions (adds ~500-1000ms LLM latency). Disabled by
            default for speed. Default: False.
        mode (Literal['query'] | Unset): Search mode discriminator Default: 'query'.
    """

    messages: list[QuerySearchRequestMessagesItem]
    repositories: list[QuerySearchRequestRepositoriesItemType1 | str] | Unset = UNSET
    data_sources: list[QuerySearchRequestDataSourcesItemType1 | str] | Unset = UNSET
    local_folders: list[QuerySearchRequestLocalFoldersItemType1 | str] | Unset = UNSET
    slack_workspaces: list[str] | Unset = UNSET
    slack_filters: None | SlackSearchFilters | Unset = UNSET
    category: None | str | Unset = UNSET
    local_source_filters: LocalSourceFilters | None | Unset = UNSET
    search_mode: str | Unset = "unified"
    stream: bool | Unset = False
    include_sources: bool | Unset = True
    fast_mode: bool | Unset = True
    skip_llm: bool | Unset = False
    reasoning_strategy: str | Unset = "vector"
    max_tokens: int | None | Unset = UNSET
    model: None | str | Unset = UNSET
    semantic_cache_threshold: float | Unset = 0.92
    bypass_semantic_cache: bool | Unset = False
    include_follow_ups: bool | Unset = False
    mode: Literal["query"] | Unset = "query"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.local_source_filters import LocalSourceFilters
        from ..models.query_search_request_data_sources_item_type_1 import QuerySearchRequestDataSourcesItemType1
        from ..models.query_search_request_local_folders_item_type_1 import QuerySearchRequestLocalFoldersItemType1
        from ..models.query_search_request_repositories_item_type_1 import QuerySearchRequestRepositoriesItemType1
        from ..models.slack_search_filters import SlackSearchFilters

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        repositories: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = []
            for repositories_item_data in self.repositories:
                repositories_item: dict[str, Any] | str
                if isinstance(repositories_item_data, QuerySearchRequestRepositoriesItemType1):
                    repositories_item = repositories_item_data.to_dict()
                else:
                    repositories_item = repositories_item_data
                repositories.append(repositories_item)

        data_sources: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.data_sources, Unset):
            data_sources = []
            for data_sources_item_data in self.data_sources:
                data_sources_item: dict[str, Any] | str
                if isinstance(data_sources_item_data, QuerySearchRequestDataSourcesItemType1):
                    data_sources_item = data_sources_item_data.to_dict()
                else:
                    data_sources_item = data_sources_item_data
                data_sources.append(data_sources_item)

        local_folders: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.local_folders, Unset):
            local_folders = []
            for local_folders_item_data in self.local_folders:
                local_folders_item: dict[str, Any] | str
                if isinstance(local_folders_item_data, QuerySearchRequestLocalFoldersItemType1):
                    local_folders_item = local_folders_item_data.to_dict()
                else:
                    local_folders_item = local_folders_item_data
                local_folders.append(local_folders_item)

        slack_workspaces: list[str] | Unset = UNSET
        if not isinstance(self.slack_workspaces, Unset):
            slack_workspaces = self.slack_workspaces

        slack_filters: dict[str, Any] | None | Unset
        if isinstance(self.slack_filters, Unset):
            slack_filters = UNSET
        elif isinstance(self.slack_filters, SlackSearchFilters):
            slack_filters = self.slack_filters.to_dict()
        else:
            slack_filters = self.slack_filters

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        local_source_filters: dict[str, Any] | None | Unset
        if isinstance(self.local_source_filters, Unset):
            local_source_filters = UNSET
        elif isinstance(self.local_source_filters, LocalSourceFilters):
            local_source_filters = self.local_source_filters.to_dict()
        else:
            local_source_filters = self.local_source_filters

        search_mode = self.search_mode

        stream = self.stream

        include_sources = self.include_sources

        fast_mode = self.fast_mode

        skip_llm = self.skip_llm

        reasoning_strategy = self.reasoning_strategy

        max_tokens: int | None | Unset
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        semantic_cache_threshold = self.semantic_cache_threshold

        bypass_semantic_cache = self.bypass_semantic_cache

        include_follow_ups = self.include_follow_ups

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if data_sources is not UNSET:
            field_dict["data_sources"] = data_sources
        if local_folders is not UNSET:
            field_dict["local_folders"] = local_folders
        if slack_workspaces is not UNSET:
            field_dict["slack_workspaces"] = slack_workspaces
        if slack_filters is not UNSET:
            field_dict["slack_filters"] = slack_filters
        if category is not UNSET:
            field_dict["category"] = category
        if local_source_filters is not UNSET:
            field_dict["local_source_filters"] = local_source_filters
        if search_mode is not UNSET:
            field_dict["search_mode"] = search_mode
        if stream is not UNSET:
            field_dict["stream"] = stream
        if include_sources is not UNSET:
            field_dict["include_sources"] = include_sources
        if fast_mode is not UNSET:
            field_dict["fast_mode"] = fast_mode
        if skip_llm is not UNSET:
            field_dict["skip_llm"] = skip_llm
        if reasoning_strategy is not UNSET:
            field_dict["reasoning_strategy"] = reasoning_strategy
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if model is not UNSET:
            field_dict["model"] = model
        if semantic_cache_threshold is not UNSET:
            field_dict["semantic_cache_threshold"] = semantic_cache_threshold
        if bypass_semantic_cache is not UNSET:
            field_dict["bypass_semantic_cache"] = bypass_semantic_cache
        if include_follow_ups is not UNSET:
            field_dict["include_follow_ups"] = include_follow_ups
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.local_source_filters import LocalSourceFilters
        from ..models.query_search_request_data_sources_item_type_1 import QuerySearchRequestDataSourcesItemType1
        from ..models.query_search_request_local_folders_item_type_1 import QuerySearchRequestLocalFoldersItemType1
        from ..models.query_search_request_messages_item import QuerySearchRequestMessagesItem
        from ..models.query_search_request_repositories_item_type_1 import QuerySearchRequestRepositoriesItemType1
        from ..models.slack_search_filters import SlackSearchFilters

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = QuerySearchRequestMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        _repositories = d.pop("repositories", UNSET)
        repositories: list[QuerySearchRequestRepositoriesItemType1 | str] | Unset = UNSET
        if _repositories is not UNSET:
            repositories = []
            for repositories_item_data in _repositories:

                def _parse_repositories_item(data: object) -> QuerySearchRequestRepositoriesItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        repositories_item_type_1 = QuerySearchRequestRepositoriesItemType1.from_dict(data)

                        return repositories_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(QuerySearchRequestRepositoriesItemType1 | str, data)

                repositories_item = _parse_repositories_item(repositories_item_data)

                repositories.append(repositories_item)

        _data_sources = d.pop("data_sources", UNSET)
        data_sources: list[QuerySearchRequestDataSourcesItemType1 | str] | Unset = UNSET
        if _data_sources is not UNSET:
            data_sources = []
            for data_sources_item_data in _data_sources:

                def _parse_data_sources_item(data: object) -> QuerySearchRequestDataSourcesItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_sources_item_type_1 = QuerySearchRequestDataSourcesItemType1.from_dict(data)

                        return data_sources_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(QuerySearchRequestDataSourcesItemType1 | str, data)

                data_sources_item = _parse_data_sources_item(data_sources_item_data)

                data_sources.append(data_sources_item)

        _local_folders = d.pop("local_folders", UNSET)
        local_folders: list[QuerySearchRequestLocalFoldersItemType1 | str] | Unset = UNSET
        if _local_folders is not UNSET:
            local_folders = []
            for local_folders_item_data in _local_folders:

                def _parse_local_folders_item(data: object) -> QuerySearchRequestLocalFoldersItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        local_folders_item_type_1 = QuerySearchRequestLocalFoldersItemType1.from_dict(data)

                        return local_folders_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(QuerySearchRequestLocalFoldersItemType1 | str, data)

                local_folders_item = _parse_local_folders_item(local_folders_item_data)

                local_folders.append(local_folders_item)

        slack_workspaces = cast(list[str], d.pop("slack_workspaces", UNSET))

        def _parse_slack_filters(data: object) -> None | SlackSearchFilters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_filters_type_0 = SlackSearchFilters.from_dict(data)

                return slack_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlackSearchFilters | Unset, data)

        slack_filters = _parse_slack_filters(d.pop("slack_filters", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_local_source_filters(data: object) -> LocalSourceFilters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                local_source_filters_type_0 = LocalSourceFilters.from_dict(data)

                return local_source_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalSourceFilters | None | Unset, data)

        local_source_filters = _parse_local_source_filters(d.pop("local_source_filters", UNSET))

        search_mode = d.pop("search_mode", UNSET)

        stream = d.pop("stream", UNSET)

        include_sources = d.pop("include_sources", UNSET)

        fast_mode = d.pop("fast_mode", UNSET)

        skip_llm = d.pop("skip_llm", UNSET)

        reasoning_strategy = d.pop("reasoning_strategy", UNSET)

        def _parse_max_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        semantic_cache_threshold = d.pop("semantic_cache_threshold", UNSET)

        bypass_semantic_cache = d.pop("bypass_semantic_cache", UNSET)

        include_follow_ups = d.pop("include_follow_ups", UNSET)

        mode = cast(Literal["query"] | Unset, d.pop("mode", UNSET))
        if mode != "query" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'query', got '{mode}'")

        query_search_request = cls(
            messages=messages,
            repositories=repositories,
            data_sources=data_sources,
            local_folders=local_folders,
            slack_workspaces=slack_workspaces,
            slack_filters=slack_filters,
            category=category,
            local_source_filters=local_source_filters,
            search_mode=search_mode,
            stream=stream,
            include_sources=include_sources,
            fast_mode=fast_mode,
            skip_llm=skip_llm,
            reasoning_strategy=reasoning_strategy,
            max_tokens=max_tokens,
            model=model,
            semantic_cache_threshold=semantic_cache_threshold,
            bypass_semantic_cache=bypass_semantic_cache,
            include_follow_ups=include_follow_ups,
            mode=mode,
        )

        query_search_request.additional_properties = d
        return query_search_request

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
