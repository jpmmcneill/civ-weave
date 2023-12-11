"""Classes pertaining to settlements in Civ Weave."""

from __future__ import annotations

from typing import NamedTuple

from yaml import safe_load

from civ_weave import data


class SettlementConfig(NamedTuple):
    """Representation of a settlement level."""

    min_population: int
    max_population: int
    num_important_features: int = 0
    num_resources: int = 0


class SettlementType(NamedTuple):
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

    hamlet: SettlementConfig | None = None
    village: SettlementConfig | None = None
    town: SettlementConfig | None = None

    @classmethod
    def from_yaml(cls) -> SettlementType:
        with data.File.settlement.get_file as s:
            settlement_data = safe_load(s)
        return cls(
            **{d.pop("name"): SettlementConfig(**d) for d in settlement_data},
        )
