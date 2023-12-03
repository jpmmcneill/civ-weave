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

    @property
    def get_file(self: File) -> TextIOWrapper:
        """Return the given file as it open(...) was called on it."""
        return Path.open(Path(__file__).parent / self.value)
