"""Classes pertaining to settlements in Civ Weave."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from yaml import safe_load

from civ_weave import data


@dataclass
class SettlementConfig:
    """Representation of a settlement level."""

    name: str
    min_population: int
    max_population: int
    num_important_features: int = 0
    num_resources: int = 0


class SettlementType(str, Enum):
    """
    Available settlement types for a given settlement.

    This could be a dynamic enum, to facilitate user customisation
    settlement types in future.

    To-Do values:
    TOWNSHIP = "township"
    SUBURB = "suburb"
    CITY = "city"
    METROPOLIS = "metropolis"
    MEGALOPOLIS = "megalopolis"
    CONURBATION = "conurbation"
    """

    HAMLET = "hamlet"
    VILLAGE = "village"
    TOWN = "town"


def _load_settlement_config() -> dict[SettlementType, SettlementConfig]:
    with data.File.settlement.get_file as s:
        settlement_data = safe_load(s)
    return {
        SettlementType(d["name"]): SettlementConfig(**d)
        for d in settlement_data
    }


SETTLEMENT_CONFIG = _load_settlement_config()
