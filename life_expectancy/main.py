""" Main script """
import argparse
from pathlib import Path
import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.load_save_data import load_data, save_data

script_dir = Path(__file__).resolve().parent
file_path = script_dir/"data"/"eu_life_expectancy_raw.tsv"

def main(country = 'PT') -> pd.DataFrame:
    """
    main function
    """
    data = load_data(file_path)
    cleaned_data = clean_data(data, country)
    save_data(cleaned_data)

    return cleaned_data

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description='Clean data and filter by country')
    parser.add_argument('--country', help='Country to use as filter')
    args = parser.parse_args()

    main(args["country"])
