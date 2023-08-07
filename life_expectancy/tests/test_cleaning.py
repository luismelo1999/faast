"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy import cleaning
from life_expectancy.regions import Region

def test_clean_data_tsv(pt_life_expectancy_expected, eu_life_expectancy_expected_tsv) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""
    cleaner = cleaning.TSVCleaner()

    pt_life_expectancy_actual = (
        cleaner.clean_data(eu_life_expectancy_expected_tsv, Region.PT)
        .reset_index(drop=True)
        )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

def test_clean_data_json(pt_life_expectancy_expected, eu_life_expectancy_raw_json) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""
    cleaner = cleaning.JSONCleaner()

    pt_life_expectancy_actual = (
        cleaner.clean_data(eu_life_expectancy_raw_json, Region.PT)
        .reset_index(drop=True)
        )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
