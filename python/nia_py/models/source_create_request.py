from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_create_request_type import SourceCreateRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_file_item import DatabaseFileItem
    from ..models.file_item import FileItem


T = TypeVar("T", bound="SourceCreateRequest")


@_attrs_define
class SourceCreateRequest:
    """
    Attributes:
        type_ (SourceCreateRequestType):
        repository (None | str | Unset):
        branch (None | str | Unset):
        ref (None | str | Unset):
        url (None | str | Unset):
        url_patterns (list[str] | None | Unset):
        exclude_patterns (list[str] | None | Unset):
        project_id (None | str | Unset):
        max_age (int | None | Unset):
        formats (list[str] | None | Unset):
        only_main_content (bool | None | Unset):
        limit (int | None | Unset):
        max_depth (int | None | Unset):
        crawl_entire_domain (bool | None | Unset):
        wait_for (int | None | Unset):
        include_screenshot (bool | None | Unset):
        check_llms_txt (bool | None | Unset):
        llms_txt_strategy (None | str | Unset):
        add_as_global_source (bool | None | Unset):  Default: True.
        is_pdf (bool | None | Unset):
        display_name (None | str | Unset):
        gcs_path (None | str | Unset):
        focus_instructions (None | str | Unset):
        extract_branding (bool | None | Unset):
        extract_images (bool | None | Unset):
        config (None | str | Unset):
        folder_name (None | str | Unset):
        folder_path (None | str | Unset):
        files (list[FileItem] | None | Unset):
        database (DatabaseFileItem | None | Unset):
        slack_installation_id (None | str | Unset):
    """

    type_: SourceCreateRequestType
    repository: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    ref: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    url_patterns: list[str] | None | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    project_id: None | str | Unset = UNSET
    max_age: int | None | Unset = UNSET
    formats: list[str] | None | Unset = UNSET
    only_main_content: bool | None | Unset = UNSET
    limit: int | None | Unset = UNSET
    max_depth: int | None | Unset = UNSET
    crawl_entire_domain: bool | None | Unset = UNSET
    wait_for: int | None | Unset = UNSET
    include_screenshot: bool | None | Unset = UNSET
    check_llms_txt: bool | None | Unset = UNSET
    llms_txt_strategy: None | str | Unset = UNSET
    add_as_global_source: bool | None | Unset = True
    is_pdf: bool | None | Unset = UNSET
    display_name: None | str | Unset = UNSET
    gcs_path: None | str | Unset = UNSET
    focus_instructions: None | str | Unset = UNSET
    extract_branding: bool | None | Unset = UNSET
    extract_images: bool | None | Unset = UNSET
    config: None | str | Unset = UNSET
    folder_name: None | str | Unset = UNSET
    folder_path: None | str | Unset = UNSET
    files: list[FileItem] | None | Unset = UNSET
    database: DatabaseFileItem | None | Unset = UNSET
    slack_installation_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_file_item import DatabaseFileItem

        type_ = self.type_.value

        repository: None | str | Unset
        if isinstance(self.repository, Unset):
            repository = UNSET
        else:
            repository = self.repository

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
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

        add_as_global_source: bool | None | Unset
        if isinstance(self.add_as_global_source, Unset):
            add_as_global_source = UNSET
        else:
            add_as_global_source = self.add_as_global_source

        is_pdf: bool | None | Unset
        if isinstance(self.is_pdf, Unset):
            is_pdf = UNSET
        else:
            is_pdf = self.is_pdf

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        gcs_path: None | str | Unset
        if isinstance(self.gcs_path, Unset):
            gcs_path = UNSET
        else:
            gcs_path = self.gcs_path

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

        config: None | str | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        else:
            config = self.config

        folder_name: None | str | Unset
        if isinstance(self.folder_name, Unset):
            folder_name = UNSET
        else:
            folder_name = self.folder_name

        folder_path: None | str | Unset
        if isinstance(self.folder_path, Unset):
            folder_path = UNSET
        else:
            folder_path = self.folder_path

        files: list[dict[str, Any]] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_dict()
                files.append(files_type_0_item)

        else:
            files = self.files

        database: dict[str, Any] | None | Unset
        if isinstance(self.database, Unset):
            database = UNSET
        elif isinstance(self.database, DatabaseFileItem):
            database = self.database.to_dict()
        else:
            database = self.database

        slack_installation_id: None | str | Unset
        if isinstance(self.slack_installation_id, Unset):
            slack_installation_id = UNSET
        else:
            slack_installation_id = self.slack_installation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if repository is not UNSET:
            field_dict["repository"] = repository
        if branch is not UNSET:
            field_dict["branch"] = branch
        if ref is not UNSET:
            field_dict["ref"] = ref
        if url is not UNSET:
            field_dict["url"] = url
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
        if gcs_path is not UNSET:
            field_dict["gcs_path"] = gcs_path
        if focus_instructions is not UNSET:
            field_dict["focus_instructions"] = focus_instructions
        if extract_branding is not UNSET:
            field_dict["extract_branding"] = extract_branding
        if extract_images is not UNSET:
            field_dict["extract_images"] = extract_images
        if config is not UNSET:
            field_dict["config"] = config
        if folder_name is not UNSET:
            field_dict["folder_name"] = folder_name
        if folder_path is not UNSET:
            field_dict["folder_path"] = folder_path
        if files is not UNSET:
            field_dict["files"] = files
        if database is not UNSET:
            field_dict["database"] = database
        if slack_installation_id is not UNSET:
            field_dict["slack_installation_id"] = slack_installation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_file_item import DatabaseFileItem
        from ..models.file_item import FileItem

        d = dict(src_dict)
        type_ = SourceCreateRequestType(d.pop("type"))

        def _parse_repository(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository = _parse_repository(d.pop("repository", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("ref", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

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

        def _parse_add_as_global_source(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        add_as_global_source = _parse_add_as_global_source(d.pop("add_as_global_source", UNSET))

        def _parse_is_pdf(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_pdf = _parse_is_pdf(d.pop("is_pdf", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_gcs_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gcs_path = _parse_gcs_path(d.pop("gcs_path", UNSET))

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

        def _parse_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_folder_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_name = _parse_folder_name(d.pop("folder_name", UNSET))

        def _parse_folder_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_path = _parse_folder_path(d.pop("folder_path", UNSET))

        def _parse_files(data: object) -> list[FileItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in _files_type_0:
                    files_type_0_item = FileItem.from_dict(files_type_0_item_data)

                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileItem] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_database(data: object) -> DatabaseFileItem | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                database_type_0 = DatabaseFileItem.from_dict(data)

                return database_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseFileItem | None | Unset, data)

        database = _parse_database(d.pop("database", UNSET))

        def _parse_slack_installation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_installation_id = _parse_slack_installation_id(d.pop("slack_installation_id", UNSET))

        source_create_request = cls(
            type_=type_,
            repository=repository,
            branch=branch,
            ref=ref,
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
            gcs_path=gcs_path,
            focus_instructions=focus_instructions,
            extract_branding=extract_branding,
            extract_images=extract_images,
            config=config,
            folder_name=folder_name,
            folder_path=folder_path,
            files=files,
            database=database,
            slack_installation_id=slack_installation_id,
        )

        source_create_request.additional_properties = d
        return source_create_request

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
