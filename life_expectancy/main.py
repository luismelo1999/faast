""" Main script """
import argparse
from pathlib import Path
import pandas as pd
from life_expectancy.cleaning import TSVCleaner, JSONCleaner
from life_expectancy.load_save_data import TSVLoader, JSONLoader, save_data
from life_expectancy.regions import Region

script_dir = Path(__file__).resolve().parent
file_path_tsv = script_dir/"data"/"eu_life_expectancy_raw.tsv"
file_path_json = script_dir/"data"/"eurostat_life_expect.json"


def main(file_path: Path, region: Region = Region.PT) -> pd.DataFrame:
    """
    main function
    """

    file_type = file_path.suffix
    if file_type == '.tsv':
        data_loader = TSVLoader()
        data_cleaner = TSVCleaner()
    elif file_type == '.json':
        data_loader = JSONLoader()
        data_cleaner = JSONCleaner()


    data = data_loader.load_data(file_path)
    cleaned_data = data_cleaner.clean_data(data, region)
    save_data(cleaned_data)

    return cleaned_data

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.file_path, args.region)
