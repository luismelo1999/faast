from pytest import MonkeyPatch
import pandas as pd

from life_expectancy.main import main



def test_main(pt_life_expectancy_expected, monkeypatch: MonkeyPatch) -> None:

    # Define a mock function to replace pd.DataFrame.to_csv
    def mock_to_csv(*args, **kwargs):
        print("Data saved successfully")

    # Patch pd.DataFrame.to_csv to return the mock function instead of the real one
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    pt_life_expectancy_actual = main(country= 'PT').reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )