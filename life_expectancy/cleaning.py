import argparse
from pathlib import Path
import pandas as pd

def load_data() -> pd.DataFrame:
    '''
    Loads the csv file that contains the data
    returns:
        data(Pandas DataFrame): Loaded dataframe

    '''

    script_dir = Path(__file__).resolve().parent
    file_path = script_dir/"data"/"eu_life_expectancy_raw.tsv"

    # load input dataframe
    data = pd.read_csv(file_path, sep='\t')

    return data

def save_data(data: pd.DataFrame) -> None:
    '''
    Saves the input dataframe into a csv file
    Args:
        data (Pandas DataFrame): DataFrame to be saved
    '''

    script_dir = Path(__file__).resolve().parent
    data.to_csv(script_dir/"data"/"pt_life_expectancy.csv", index=False)

def clean_data(data: pd.DataFrame, country: str = 'PT'):
    '''
    Cleans and filters the input data
    Args:
        data (Pandas DataFrame): DataFrame to be cleaned
        country (str): String with country
    returns:
        filtered_df (Pandas DataFrame): Dataframe cleaned an filtered
    '''

    ids = ['unit', 'sex', 'age', 'region']
    # split the first columns into 4 diferent columns using , as separator
    data[ids] = data['unit,sex,age,geo\\time'].str.split(',', expand=True)

    # drop unecessary column
    data = data.drop(columns=['unit,sex,age,geo\\time'])

    # unpivot the dataset to long format
    melted_df = pd.melt(data, value_vars = data.drop(columns = ids).columns,
          id_vars = ids, var_name = 'year', value_name='value')

    # ensures year is a int
    melted_df['year'] = melted_df['year'].astype(int)

    # cleans column value and ensures value is a float
    melted_df['value'] = (melted_df['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    cleaned_df = melted_df.dropna()

    # filter for country
    filtered_df = cleaned_df[cleaned_df['region'] == country]

    return filtered_df

def main(country = 'PT'):
    """
    main function
    """
    data = load_data()
    cleaned_data = clean_data(data, country)
    save_data(cleaned_data)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description='Clean data and filter by country')
    parser.add_argument('--country', help='Country to use as filter')
    args = parser.parse_args()

    main(args["country"])
