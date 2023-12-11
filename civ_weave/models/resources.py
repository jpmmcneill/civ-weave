"""Classes pertaining to resources in Civ Weave."""

# an important thing here is fantasy level...
# there should probably be a few preset fantasy levels. Namely low medium high
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from yaml import safe_load

from civ_weave import data


class FantasyLevel(float, Enum):
    LOW = 1
    MIDDLE = 1.5
    HIGH = 2.3


@dataclass
class RarityConfig:
    name: str
    description: str
    creation_probability: float


class RarityType(str, Enum):
    abundant = "Abundant"
    common = "Common"
    uncommon = "Uncommon"
    rare = "Rare"
    very_rare = "Very Rare"
    legendary = "Legendary"
    mythical = "Mythical"

    @staticmethod
    def get_probability(index: int, parameter: float):
        weights = [1 / parameter**x for x in range(7)]
        sum(weights)
        # return weights[index] / total
        return weights


@dataclass
class ResourceConfig:
    name: str
    description: str
    resource_type: str
    rarity: RarityType


def _load_rarity_config() -> dict[RarityType, RarityConfig]:
    with data.File.rarity.get_file as s:
        rarity_data = safe_load(s)
    return {RarityType(d["name"]): RarityConfig(**d) for d in rarity_data}
