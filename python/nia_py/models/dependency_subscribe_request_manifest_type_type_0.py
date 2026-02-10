from enum import Enum


class DependencySubscribeRequestManifestTypeType0(str, Enum):
    CARGO_TOML = "Cargo.toml"
    GEMFILE = "Gemfile"
    GO_MOD = "go.mod"
    PACKAGE_JSON = "package.json"
    PYPROJECT_TOML = "pyproject.toml"
    REQUIREMENTS_TXT = "requirements.txt"

    def __str__(self) -> str:
        return str(self.value)
