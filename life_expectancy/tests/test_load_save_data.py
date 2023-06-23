"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.load_save_data import load_data, save_data
from pytest import MonkeyPatch
from . import OUTPUT_DIR


def test_load_data(eu_life_expectancy_expected)-> None:
    """Run the `load_data` function and compare the output to the expected output"""
    eu_life_expectancy_actual = load_data(OUTPUT_DIR / "eu_life_expectancy_raw.tsv")

    pd.testing.assert_frame_equal(
        eu_life_expectancy_actual, eu_life_expectancy_expected
    )

def test_save_data(
        monkeypatch: MonkeyPatch,
        capsys, 
        pt_life_expectancy_expected
    ) -> None:

    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    # Call the save_data function and get the result
    save_data(pt_life_expectancy_expected)

    captured = capsys.readouterr()

    assert "Data saved successfully" in captured.out