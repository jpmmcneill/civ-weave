"""Module containing classes use in interacting with the Civ Weave backend."""

from functools import cache

from civ_weave.components.settlement import SettlementType


@cache
def get_settlement_types() -> SettlementType:
    """Return configured settlement types."""
    return SettlementType.from_yaml()
