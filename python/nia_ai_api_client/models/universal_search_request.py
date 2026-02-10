from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.universal_search_request_boost_source_types import UniversalSearchRequestBoostSourceTypes


T = TypeVar("T", bound="UniversalSearchRequest")


@_attrs_define
class UniversalSearchRequest:
    """
    Attributes:
        query (str): Natural language search query
        top_k (int | Unset): Total number of results Default: 20.
        include_repos (bool | Unset): Include repository sources Default: True.
        include_docs (bool | Unset): Include documentation sources Default: True.
        include_huggingface_datasets (bool | Unset): Include HuggingFace dataset sources (excluded by default to prevent
            search pollution) Default: False.
        alpha (float | Unset): Weight for vector search (0.7 = 70% vector) Default: 0.7.
        compress_output (bool | Unset): Use AI to compress results Default: False.
        max_sources (int | Unset): Max source namespaces to deep search Default: 5.
        sources_for_answer (int | Unset): Number of results to use for AI answer Default: 10.
        bypass_cache (bool | Unset): Skip cache and force fresh search results Default: False.
        max_tokens (int | None | Unset): Maximum tokens in response. Results truncated when budget reached.
        boost_source_types (UniversalSearchRequestBoostSourceTypes | Unset): Source type boosts (override to customize
            or set {} to disable)
        boost_languages (list[str] | None | Unset): Programming languages to boost (e.g., ['python', 'typescript'])
        language_boost_factor (float | Unset): Boost multiplier for preferred languages Default: 1.5.
        use_native_boosting (bool | Unset): Use TurboPuffer FTS v2 native Sum/Product boosting Default: True.
        semantic_cache_threshold (float | Unset): Minimum similarity for semantic cache hit (0.8-1.0) Default: 0.92.
        bypass_semantic_cache (bool | Unset): Skip semantic cache (L2) lookup Default: False.
        expand_symbols (bool | Unset): Extract function/class names from results and search for usages (cAST-inspired)
            Default: False.
    """

    query: str
    top_k: int | Unset = 20
    include_repos: bool | Unset = True
    include_docs: bool | Unset = True
    include_huggingface_datasets: bool | Unset = False
    alpha: float | Unset = 0.7
    compress_output: bool | Unset = False
    max_sources: int | Unset = 5
    sources_for_answer: int | Unset = 10
    bypass_cache: bool | Unset = False
    max_tokens: int | None | Unset = UNSET
    boost_source_types: UniversalSearchRequestBoostSourceTypes | Unset = UNSET
    boost_languages: list[str] | None | Unset = UNSET
    language_boost_factor: float | Unset = 1.5
    use_native_boosting: bool | Unset = True
    semantic_cache_threshold: float | Unset = 0.92
    bypass_semantic_cache: bool | Unset = False
    expand_symbols: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        top_k = self.top_k

        include_repos = self.include_repos

        include_docs = self.include_docs

        include_huggingface_datasets = self.include_huggingface_datasets

        alpha = self.alpha

        compress_output = self.compress_output

        max_sources = self.max_sources

        sources_for_answer = self.sources_for_answer

        bypass_cache = self.bypass_cache

        max_tokens: int | None | Unset
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        boost_source_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.boost_source_types, Unset):
            boost_source_types = self.boost_source_types.to_dict()

        boost_languages: list[str] | None | Unset
        if isinstance(self.boost_languages, Unset):
            boost_languages = UNSET
        elif isinstance(self.boost_languages, list):
            boost_languages = self.boost_languages

        else:
            boost_languages = self.boost_languages

        language_boost_factor = self.language_boost_factor

        use_native_boosting = self.use_native_boosting

        semantic_cache_threshold = self.semantic_cache_threshold

        bypass_semantic_cache = self.bypass_semantic_cache

        expand_symbols = self.expand_symbols

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if include_repos is not UNSET:
            field_dict["include_repos"] = include_repos
        if include_docs is not UNSET:
            field_dict["include_docs"] = include_docs
        if include_huggingface_datasets is not UNSET:
            field_dict["include_huggingface_datasets"] = include_huggingface_datasets
        if alpha is not UNSET:
            field_dict["alpha"] = alpha
        if compress_output is not UNSET:
            field_dict["compress_output"] = compress_output
        if max_sources is not UNSET:
            field_dict["max_sources"] = max_sources
        if sources_for_answer is not UNSET:
            field_dict["sources_for_answer"] = sources_for_answer
        if bypass_cache is not UNSET:
            field_dict["bypass_cache"] = bypass_cache
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if boost_source_types is not UNSET:
            field_dict["boost_source_types"] = boost_source_types
        if boost_languages is not UNSET:
            field_dict["boost_languages"] = boost_languages
        if language_boost_factor is not UNSET:
            field_dict["language_boost_factor"] = language_boost_factor
        if use_native_boosting is not UNSET:
            field_dict["use_native_boosting"] = use_native_boosting
        if semantic_cache_threshold is not UNSET:
            field_dict["semantic_cache_threshold"] = semantic_cache_threshold
        if bypass_semantic_cache is not UNSET:
            field_dict["bypass_semantic_cache"] = bypass_semantic_cache
        if expand_symbols is not UNSET:
            field_dict["expand_symbols"] = expand_symbols

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.universal_search_request_boost_source_types import UniversalSearchRequestBoostSourceTypes

        d = dict(src_dict)
        query = d.pop("query")

        top_k = d.pop("top_k", UNSET)

        include_repos = d.pop("include_repos", UNSET)

        include_docs = d.pop("include_docs", UNSET)

        include_huggingface_datasets = d.pop("include_huggingface_datasets", UNSET)

        alpha = d.pop("alpha", UNSET)

        compress_output = d.pop("compress_output", UNSET)

        max_sources = d.pop("max_sources", UNSET)

        sources_for_answer = d.pop("sources_for_answer", UNSET)

        bypass_cache = d.pop("bypass_cache", UNSET)

        def _parse_max_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        _boost_source_types = d.pop("boost_source_types", UNSET)
        boost_source_types: UniversalSearchRequestBoostSourceTypes | Unset
        if isinstance(_boost_source_types, Unset):
            boost_source_types = UNSET
        else:
            boost_source_types = UniversalSearchRequestBoostSourceTypes.from_dict(_boost_source_types)

        def _parse_boost_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                boost_languages_type_0 = cast(list[str], data)

                return boost_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        boost_languages = _parse_boost_languages(d.pop("boost_languages", UNSET))

        language_boost_factor = d.pop("language_boost_factor", UNSET)

        use_native_boosting = d.pop("use_native_boosting", UNSET)

        semantic_cache_threshold = d.pop("semantic_cache_threshold", UNSET)

        bypass_semantic_cache = d.pop("bypass_semantic_cache", UNSET)

        expand_symbols = d.pop("expand_symbols", UNSET)

        universal_search_request = cls(
            query=query,
            top_k=top_k,
            include_repos=include_repos,
            include_docs=include_docs,
            include_huggingface_datasets=include_huggingface_datasets,
            alpha=alpha,
            compress_output=compress_output,
            max_sources=max_sources,
            sources_for_answer=sources_for_answer,
            bypass_cache=bypass_cache,
            max_tokens=max_tokens,
            boost_source_types=boost_source_types,
            boost_languages=boost_languages,
            language_boost_factor=language_boost_factor,
            use_native_boosting=use_native_boosting,
            semantic_cache_threshold=semantic_cache_threshold,
            bypass_semantic_cache=bypass_semantic_cache,
            expand_symbols=expand_symbols,
        )

        universal_search_request.additional_properties = d
        return universal_search_request

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
