from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceRequest")


@_attrs_define
class DataSourceRequest:
    """
    Attributes:
        url (str): URL to index (documentation or website)
        url_patterns (list[str] | None | Unset): URL patterns to include in crawling (supports wildcards)
        exclude_patterns (list[str] | None | Unset): URL patterns to exclude from crawling (supports wildcards)
        project_id (None | str | Unset): Optional project ID to associate with
        max_age (int | None | Unset): Maximum age of cached content in seconds (default: 0 / always fresh) Default: 0.
        formats (list[str] | None | Unset): Content formats to return (e.g., ['markdown', 'html'])
        only_main_content (bool | None | Unset): Extract only main content (False recommended for JS-heavy sites)
            Default: False.
        limit (int | None | Unset): Maximum number of pages to crawl (default: 10000) Default: 10000.
        max_depth (int | None | Unset): Maximum crawl depth (default: 20) Default: 20.
        crawl_entire_domain (bool | None | Unset): Whether to crawl the entire domain (default: True) Default: True.
        wait_for (int | None | Unset): Time to wait for page to load in milliseconds (default: 2000ms for JS-heavy
            sites) Default: 2000.
        include_screenshot (bool | None | Unset): Include full page screenshot (default: False) Default: False.
        check_llms_txt (bool | None | Unset): Check for llms.txt file for curated documentation URLs (default: True)
            Default: True.
        llms_txt_strategy (None | str | Unset): How to use llms.txt: 'prefer' (start with llms.txt URLs then crawl
            more), 'only' (only llms.txt URLs), 'ignore' (skip llms.txt check) Default: 'prefer'.
        add_as_global_source (bool | Unset): Add to global shared pool (default: True). Set False for private indexing.
            Default: True.
        is_pdf (bool | Unset): Whether this is a direct PDF URL (disables crawling, uses longer timeout) Default: False.
        display_name (None | str | Unset): Custom display name for the source
        focus_instructions (None | str | Unset): Natural language instructions for what content to include (uses LLM
            filtering)
        extract_branding (bool | None | Unset): Extract brand identity and design system (colors, logos, fonts) Default:
            False.
        extract_images (bool | None | Unset): Extract all image URLs from the page Default: False.
    """

    url: str
    url_patterns: list[str] | None | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    project_id: None | str | Unset = UNSET
    max_age: int | None | Unset = 0
    formats: list[str] | None | Unset = UNSET
    only_main_content: bool | None | Unset = False
    limit: int | None | Unset = 10000
    max_depth: int | None | Unset = 20
    crawl_entire_domain: bool | None | Unset = True
    wait_for: int | None | Unset = 2000
    include_screenshot: bool | None | Unset = False
    check_llms_txt: bool | None | Unset = True
    llms_txt_strategy: None | str | Unset = "prefer"
    add_as_global_source: bool | Unset = True
    is_pdf: bool | Unset = False
    display_name: None | str | Unset = UNSET
    focus_instructions: None | str | Unset = UNSET
    extract_branding: bool | None | Unset = False
    extract_images: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        url_patterns: list[str] | None | Unset
        if isinstance(self.url_patterns, Unset):
            url_patterns = UNSET
        elif isinstance(self.url_patterns, list):
            url_patterns = self.url_patterns

        else:
            url_patterns = self.url_patterns

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        max_age: int | None | Unset
        if isinstance(self.max_age, Unset):
            max_age = UNSET
        else:
            max_age = self.max_age

        formats: list[str] | None | Unset
        if isinstance(self.formats, Unset):
            formats = UNSET
        elif isinstance(self.formats, list):
            formats = self.formats

        else:
            formats = self.formats

        only_main_content: bool | None | Unset
        if isinstance(self.only_main_content, Unset):
            only_main_content = UNSET
        else:
            only_main_content = self.only_main_content

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        max_depth: int | None | Unset
        if isinstance(self.max_depth, Unset):
            max_depth = UNSET
        else:
            max_depth = self.max_depth

        crawl_entire_domain: bool | None | Unset
        if isinstance(self.crawl_entire_domain, Unset):
            crawl_entire_domain = UNSET
        else:
            crawl_entire_domain = self.crawl_entire_domain

        wait_for: int | None | Unset
        if isinstance(self.wait_for, Unset):
            wait_for = UNSET
        else:
            wait_for = self.wait_for

        include_screenshot: bool | None | Unset
        if isinstance(self.include_screenshot, Unset):
            include_screenshot = UNSET
        else:
            include_screenshot = self.include_screenshot

        check_llms_txt: bool | None | Unset
        if isinstance(self.check_llms_txt, Unset):
            check_llms_txt = UNSET
        else:
            check_llms_txt = self.check_llms_txt

        llms_txt_strategy: None | str | Unset
        if isinstance(self.llms_txt_strategy, Unset):
            llms_txt_strategy = UNSET
        else:
            llms_txt_strategy = self.llms_txt_strategy

        add_as_global_source = self.add_as_global_source

        is_pdf = self.is_pdf

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        focus_instructions: None | str | Unset
        if isinstance(self.focus_instructions, Unset):
            focus_instructions = UNSET
        else:
            focus_instructions = self.focus_instructions

        extract_branding: bool | None | Unset
        if isinstance(self.extract_branding, Unset):
            extract_branding = UNSET
        else:
            extract_branding = self.extract_branding

        extract_images: bool | None | Unset
        if isinstance(self.extract_images, Unset):
            extract_images = UNSET
        else:
            extract_images = self.extract_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if url_patterns is not UNSET:
            field_dict["url_patterns"] = url_patterns
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if max_age is not UNSET:
            field_dict["max_age"] = max_age
        if formats is not UNSET:
            field_dict["formats"] = formats
        if only_main_content is not UNSET:
            field_dict["only_main_content"] = only_main_content
        if limit is not UNSET:
            field_dict["limit"] = limit
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth
        if crawl_entire_domain is not UNSET:
            field_dict["crawl_entire_domain"] = crawl_entire_domain
        if wait_for is not UNSET:
            field_dict["wait_for"] = wait_for
        if include_screenshot is not UNSET:
            field_dict["include_screenshot"] = include_screenshot
        if check_llms_txt is not UNSET:
            field_dict["check_llms_txt"] = check_llms_txt
        if llms_txt_strategy is not UNSET:
            field_dict["llms_txt_strategy"] = llms_txt_strategy
        if add_as_global_source is not UNSET:
            field_dict["add_as_global_source"] = add_as_global_source
        if is_pdf is not UNSET:
            field_dict["is_pdf"] = is_pdf
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if focus_instructions is not UNSET:
            field_dict["focus_instructions"] = focus_instructions
        if extract_branding is not UNSET:
            field_dict["extract_branding"] = extract_branding
        if extract_images is not UNSET:
            field_dict["extract_images"] = extract_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_url_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                url_patterns_type_0 = cast(list[str], data)

                return url_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        url_patterns = _parse_url_patterns(d.pop("url_patterns", UNSET))

        def _parse_exclude_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_patterns_type_0 = cast(list[str], data)

                return exclude_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_patterns = _parse_exclude_patterns(d.pop("exclude_patterns", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_max_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_age = _parse_max_age(d.pop("max_age", UNSET))

        def _parse_formats(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = cast(list[str], data)

                return formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        formats = _parse_formats(d.pop("formats", UNSET))

        def _parse_only_main_content(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        only_main_content = _parse_only_main_content(d.pop("only_main_content", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_max_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_depth = _parse_max_depth(d.pop("max_depth", UNSET))

        def _parse_crawl_entire_domain(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        crawl_entire_domain = _parse_crawl_entire_domain(d.pop("crawl_entire_domain", UNSET))

        def _parse_wait_for(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wait_for = _parse_wait_for(d.pop("wait_for", UNSET))

        def _parse_include_screenshot(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_screenshot = _parse_include_screenshot(d.pop("include_screenshot", UNSET))

        def _parse_check_llms_txt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        check_llms_txt = _parse_check_llms_txt(d.pop("check_llms_txt", UNSET))

        def _parse_llms_txt_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llms_txt_strategy = _parse_llms_txt_strategy(d.pop("llms_txt_strategy", UNSET))

        add_as_global_source = d.pop("add_as_global_source", UNSET)

        is_pdf = d.pop("is_pdf", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_focus_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        focus_instructions = _parse_focus_instructions(d.pop("focus_instructions", UNSET))

        def _parse_extract_branding(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        extract_branding = _parse_extract_branding(d.pop("extract_branding", UNSET))

        def _parse_extract_images(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        extract_images = _parse_extract_images(d.pop("extract_images", UNSET))

        data_source_request = cls(
            url=url,
            url_patterns=url_patterns,
            exclude_patterns=exclude_patterns,
            project_id=project_id,
            max_age=max_age,
            formats=formats,
            only_main_content=only_main_content,
            limit=limit,
            max_depth=max_depth,
            crawl_entire_domain=crawl_entire_domain,
            wait_for=wait_for,
            include_screenshot=include_screenshot,
            check_llms_txt=check_llms_txt,
            llms_txt_strategy=llms_txt_strategy,
            add_as_global_source=add_as_global_source,
            is_pdf=is_pdf,
            display_name=display_name,
            focus_instructions=focus_instructions,
            extract_branding=extract_branding,
            extract_images=extract_images,
        )

        data_source_request.additional_properties = d
        return data_source_request

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
