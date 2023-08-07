""" Cleaning data script """
from abc import ABC, abstractmethod
import pandas as pd
from life_expectancy.regions import Region

# Define the strategy interface
class DataCleanerStrategy(ABC):
    """Abstract class for cleaning data"""

    @abstractmethod
    def clean_data(self, data: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Abstract method to clean the data"""

# Concrete strategy classes
class TSVCleaner(DataCleanerStrategy):
    """class for cleaning TSV data"""

    def clean_data(self, data: pd.DataFrame, region: Region) -> pd.DataFrame:
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
        filtered_df = cleaned_df[cleaned_df['region'] == region.value]

        return filtered_df

class JSONCleaner(DataCleanerStrategy):
    """class for cleaning JSON data"""

    def clean_data(self, data: pd.DataFrame, region: Region) -> pd.DataFrame:
        '''
        Cleans and filters the input data
        Args:
            data (Pandas DataFrame): DataFrame to be cleaned
            country (str): String with country
        returns:
            filtered_df (Pandas DataFrame): Dataframe cleaned an filtered
        '''

        renamed_df = data.rename(columns={"country": "region", "life_expectancy": "value"})

        cleaned_df = renamed_df.drop(columns=["flag", "flag_detail"], axis = 1)

        filtered_df = cleaned_df[cleaned_df["region"] == region.value]

        return filtered_df
