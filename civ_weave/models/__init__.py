"""Module containing classes use in interacting with the Civ Weave backend."""

from functools import cache

from civ_weave.models.settlement import SettlementType


@cache
def get_settlement_types() -> SettlementType:
    return SettlementType.from_yaml()
