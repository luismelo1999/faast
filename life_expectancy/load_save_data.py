""" Load and save data script """
from pathlib import Path
from abc import ABC, abstractmethod
import pandas as pd


# Define the strategy interface
class DataLoaderStrategy(ABC):
    """Abstract class for loading data"""
    @abstractmethod
    def load_data(self, file_path):
        """Abstract method to load the data"""

# Concrete strategy classes
class TSVLoader(DataLoaderStrategy):
    """class for loading TSV data"""

    def load_data(self, file_path) -> pd.DataFrame:
        '''
        Loads the csv file that contains the data
        returns:
            data(Pandas DataFrame): Loaded dataframe
        '''

        # load input tsv dataframe
        return pd.read_csv(file_path, sep='\t')

class JSONLoader(DataLoaderStrategy):
    """class for cleaning JSON data"""

    def load_data(self, file_path):
        '''
        Loads the json file that contains the data
        returns:
            data(Pandas DataFrame): Loaded dataframe
        '''

        # load input json dataframe
        return pd.read_json(file_path, compression="infer")

def save_data(data: pd.DataFrame) -> None:
    '''
    Saves the input dataframe into a csv file
    Args:
        data (Pandas DataFrame): DataFrame to be saved
    '''

    script_dir = Path(__file__).resolve().parent
    data.to_csv(script_dir/"data"/"pt_life_expectancy.csv", index=False)
