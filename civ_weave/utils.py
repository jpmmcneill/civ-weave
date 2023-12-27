"""Utility Functions in civ-weave."""

from __future__ import annotations

from random import choice, uniform
from typing import Iterable, TypeVar

T = TypeVar("T")


def random_choice(
    objects: Iterable[T],
    prob_attribute: str | None = "probability",
) -> T:
    """
    Choose from a subscriptable iterable of classes.

    This supports either a random choice from the given iterable,
    or a probabilistic choice based on an attribute of the given class.

    Args:
    ----
        objects (Iterable[T]): A subscriptable iterable of objects.
          These may be of different types in principle.
        prob_attribute (str = "probability"): The attribute of each element of
          objects to use as a probability for choice when uniform_probs is set
          to False. When `None` is passed, the objects are chosen with equal
          probabilities.

    Returns:
    -------
        Clazz (object): The randomly chosen element of objects.
    """
    if prob_attribute is None:
        return choice(objects)
    csum = 0
    rndm_choice = uniform(0, 1)
    # could build a module level dict that has each objects as a key
    # and the csum array stored?
    for clazz in objects:
        csum += getattr(clazz, prob_attribute)
        if rndm_choice <= csum:
            return clazz
    return objects[-1]
