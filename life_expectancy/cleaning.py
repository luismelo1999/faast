import argparse
import pandas as pd

def clean_data(country = 'PT'):
    '''
    Cleans the data
    '''
    # load input dataframe
    life_expectancy = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')

    ids = ['unit', 'sex', 'age', 'region']
    # split the first columns into 4 diferent columns using , as separator
    life_expectancy[ids] = life_expectancy['unit,sex,age,geo\\time'].str.split(',', expand=True)

    # drop unecessary column
    life_expectancy = life_expectancy.drop(columns=['unit,sex,age,geo\\time'])

    # unpivot the dataset to long format
    melted_df = pd.melt(life_expectancy, value_vars = life_expectancy.drop(columns = ids).columns,
          id_vars = ids, var_name = 'year', value_name='value')

    # ensures year is a int
    melted_df['year'] = melted_df['year'].astype(int)

    # cleans column value and ensures value is a float
    melted_df['value'] = (melted_df['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    cleaned_df = melted_df.dropna()

    filtered_df = cleaned_df[cleaned_df['region'] == country]

    filtered_df.to_csv('life_expectancy/data/pt_life_expectancy.csv', index = False)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description='Clean data and filter by country')
    parser.add_argument('--country', help='Country to use as filter')
    args = parser.parse_args()
    clean_data(args)