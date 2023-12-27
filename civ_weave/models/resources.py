"""Classes pertaining to resources in Civ Weave."""

from __future__ import annotations

from copy import deepcopy
from functools import cache
from typing import NamedTuple

from yaml import safe_load

from civ_weave import data
from civ_weave.utils import random_choice


class Resource(NamedTuple):
    """Resource that is available to a settlement."""

    name: str
    description: str
    resource_type: str
    typical_use: str


class Rarity(NamedTuple):
    """Rarity of a given set of resources."""

    name: str
    probability: float


# perhaps we should care about fantasy level in here?
# this would impact the probabilities for each rarity level
class RarityLevels(NamedTuple):
    """Resource Levels configured for the resource generator."""

    common: Rarity | None = None
    uncommon: Rarity | None = None
    rare: Rarity | None = None
    very_rare: Rarity | None = None
    legendary: Rarity | None = None
    mythical: Rarity | None = None


@cache
def _get_rarity_levels() -> RarityLevels:
    """Load Rarity Type configuration data from the yaml configuration."""
    with data.File.resource_rarity.get_file as s:
        settlement_data = safe_load(s)
    return RarityLevels(
        **{d["name"]: Rarity(**d) for d in settlement_data},
    )


@cache
def _get_resources() -> dict[Rarity, set[Resource]]:
    """Load Resource data from the yaml configuration."""
    with data.File.resource.get_file as s:
        resource_data = safe_load(s)
    rarity_levels = _get_rarity_levels()
    return {
        getattr(rarity_levels, level): {
            Resource(**resource) for resource in values
        }
        for level, values in resource_data.items()
    }


class ResourceBucket:
    """Class for generation of random resources."""

    levels: RarityLevels
    resources: dict[Rarity, set[Resource]]

    def __init__(self: ResourceBucket) -> None:
        """Initialise a resource bucket, with fresh resources and levels."""
        self.levels = deepcopy(_get_rarity_levels())
        self.resources = deepcopy(_get_resources())

    def _remove_resource(
        self: ResourceBucket,
        level: Rarity,
        resource: Resource,
    ) -> None:
        self.resources[level].remove(resource)

    def draw_rarity_level(self: ResourceBucket) -> Rarity:
        """Get a random rarity level based on rarity level probabilities."""
        return random_choice(self.levels)

    def draw_resource(
        self: ResourceBucket,
        *,
        remove_after_choice: bool = True,
    ) -> tuple[Rarity, Resource]:
        """
        Get a random resource.

        This first generates a rarity level as a sample, and then
        fetches a resource from the resources under that rarity level.

        This (by default) removes the drawn resource from the bucket
        that is be used for future draws from the instance.
        """
        level = self.draw_rarity_level()
        resource = random_choice(
            list(self.resources[level]),
            prob_attribute=None,
        )

        if remove_after_choice:
            self._remove_resource(level, resource)

        return level, resource
