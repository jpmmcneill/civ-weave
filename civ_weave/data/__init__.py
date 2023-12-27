"""Data pertaining to Civ Weave config."""
from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import TextIOWrapper


class File(str, Enum):
    """Wrapper to access a file in the data directory."""

    settlement = "settlement.yml"
    resource_rarity = "resource_rarity.yml"
    resource = "resource.yml"

    @property
    def get_file(self: File) -> TextIOWrapper:
        """Return the given file as it open(...) was called on it."""
        return Path.open(self.get_path)

    @property
    def get_path(self: File) -> Path:
        """Return the file path for the given File."""
        return Path(__file__).parent / self.value
