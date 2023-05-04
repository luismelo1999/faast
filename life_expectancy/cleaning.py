import argparse
import pandas as pd

def load_data():
    '''
    Cleans the data
    '''
    # load input dataframe
    data = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')

    return data

def save_data(data):
    '''
    Cleans the data
    '''

    data.to_csv('life_expectancy/data/pt_life_expectancy.csv', index = False)

def clean_data(data, country = 'PT'):
    '''
    Cleans the data
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
