from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.source_type_summary import SourceTypeSummary


T = TypeVar("T", bound="SourcesSummaryResponse")


@_attrs_define
class SourcesSummaryResponse:
    """
    Attributes:
        repositories (SourceTypeSummary):
        documentation (SourceTypeSummary):
        research_papers (SourceTypeSummary):
        huggingface_datasets (SourceTypeSummary):
        local_folders (SourceTypeSummary):
        slack (SourceTypeSummary):
        google_drive (SourceTypeSummary):
    """

    repositories: SourceTypeSummary
    documentation: SourceTypeSummary
    research_papers: SourceTypeSummary
    huggingface_datasets: SourceTypeSummary
    local_folders: SourceTypeSummary
    slack: SourceTypeSummary
    google_drive: SourceTypeSummary
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repositories = self.repositories.to_dict()

        documentation = self.documentation.to_dict()

        research_papers = self.research_papers.to_dict()

        huggingface_datasets = self.huggingface_datasets.to_dict()

        local_folders = self.local_folders.to_dict()

        slack = self.slack.to_dict()

        google_drive = self.google_drive.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositories": repositories,
                "documentation": documentation,
                "research_papers": research_papers,
                "huggingface_datasets": huggingface_datasets,
                "local_folders": local_folders,
                "slack": slack,
                "google_drive": google_drive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_type_summary import SourceTypeSummary

        d = dict(src_dict)
        repositories = SourceTypeSummary.from_dict(d.pop("repositories"))

        documentation = SourceTypeSummary.from_dict(d.pop("documentation"))

        research_papers = SourceTypeSummary.from_dict(d.pop("research_papers"))

        huggingface_datasets = SourceTypeSummary.from_dict(d.pop("huggingface_datasets"))

        local_folders = SourceTypeSummary.from_dict(d.pop("local_folders"))

        slack = SourceTypeSummary.from_dict(d.pop("slack"))

        google_drive = SourceTypeSummary.from_dict(d.pop("google_drive"))

        sources_summary_response = cls(
            repositories=repositories,
            documentation=documentation,
            research_papers=research_papers,
            huggingface_datasets=huggingface_datasets,
            local_folders=local_folders,
            slack=slack,
            google_drive=google_drive,
        )

        sources_summary_response.additional_properties = d
        return sources_summary_response

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
