"""Tests relating to Settlement Models."""
from __future__ import annotations

from importlib.resources import files
from pathlib import Path
from unittest import TestCase
from unittest.mock import PropertyMock, patch

from civ_weave.components.settlement import SettlementConfig, SettlementType
from tests import data as test_data


class TestSettlementType(TestCase):
    """Tests relating to the Settlement Type Class."""

    def test_from_yaml(self: TestSettlementType) -> None:
        """Check that the base yaml configuration loads correctly."""
        SettlementType.from_yaml()

    @patch("civ_weave.data.File.get_path", new_callable=PropertyMock)
    def test_yaml_content(
        self: TestSettlementType,
        get_path: PropertyMock,
    ) -> None:
        """Check that test settlement type data is parsed correctly."""
        get_path.return_value = Path(
            files(test_data) / "settlement_test_data.yml",
        )

        expected_result = SettlementType(
            hamlet=SettlementConfig(
                min_population=50,
                max_population=100,
            ),
            village=SettlementConfig(
                min_population=200,
                max_population=500,
            ),
        )

        result = SettlementType.from_yaml()

        self.assertEqual(result, expected_result)
