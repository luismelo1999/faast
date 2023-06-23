""" Load and save data script """
from pathlib import Path
import pandas as pd

def load_data(file_path) -> pd.DataFrame:
    '''
    Loads the csv file that contains the data
    returns:
        data(Pandas DataFrame): Loaded dataframe

    '''

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
