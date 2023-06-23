"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import clean_data

def test_clean_data(pt_life_expectancy_expected, eu_life_expectancy_expected) -> None:
    """Run the `clean_data` function and compare the output to the expected output"""
    pt_life_expectancy_actual = clean_data(eu_life_expectancy_expected, country='PT').reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
