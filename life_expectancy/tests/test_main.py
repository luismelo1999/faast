"""Tests for the main module"""
from pytest import MonkeyPatch
import pandas as pd
from life_expectancy.main import main
from life_expectancy.regions import Region
from . import OUTPUT_DIR

def test_main_tsv(pt_life_expectancy_expected, monkeypatch: MonkeyPatch) -> None:
    """Run the `main` function and compare the output to the expected output"""

    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    pt_life_expectancy_actual = main(
            OUTPUT_DIR / "eu_life_expectancy_raw.tsv",
            Region.PT
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

def test_main_json(pt_life_expectancy_expected, monkeypatch: MonkeyPatch) -> None:
    """Run the `main` function and compare the output to the expected output"""

    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    pt_life_expectancy_actual = main(
            OUTPUT_DIR / "eurostat_life_expect.json",
            Region.PT
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
