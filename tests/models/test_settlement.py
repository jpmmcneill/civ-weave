from importlib.resources import files
from pathlib import Path
from unittest.mock import PropertyMock, patch

from civ_weave.models.settlement import SettlementConfig, SettlementType
from tests import data as test_data


def test_from_yaml():
    """Assert that the base yaml configuration loads correctly."""
    SettlementType.from_yaml()

@patch("civ_weave.data.File.get_path", new_callable=PropertyMock)
def test_yaml_content(get_path: PropertyMock):
    get_path.return_value = Path(files(test_data) / "settlement_test_data.yml")

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

    assert result == expected_result
