import numpy as np
import pandas as pd

ages = pd.Series()

def main():
    data = pd.Series([0.25, 0.5, 0.75, 1.0],
                     index=['a','b','c','d'])
    print(data)
    print(data['b'])
    population_dict = {'California': 39538223, 'Texas': 29145505,
                   'Florida': 21538187, 'New York': 20201249,
                   'Pennsylvania': 13002700}
    population = pd.Series(population_dict)
    print(population['California'])
    print(population['California':'Florida'])
    month = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    print(month)
    # Series have attributes values & index
    print(month.values) # looks like a list
    print(month.index) # reveals shwows range of nums
    
    #index explicitly
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    better_month = pd.Series(month_list,
                            index=[1,2,3,4,5,6,7,8,9,10,11,12])
    
    print(better_month)

    # Access value @ index
    print(f'My birthday is in {better_month[7]}')

    # Can also think of Series like a simple dictionary
    birth_months = {'Kevin':'Mar',
                    'Jackson':'Aug',
                    'Finny':'Jul',
                    'Bryce':'Nov',
                    'Natalie':'Mar',
                    'Paige':'Feb',
                    'Maia': 'Apr'}
    birth_series = pd.Series(birth_months)
    print(birth_series)

    # create a dataframe from a single series object
    df = pd.DataFrame(birth_series, columns=['Birth Month'])
    print(df) # DataFrame objects have column headers
    
    # Create a DataFrame from dictionaries

    pokemon_df = pd.read_csv('pokemon_data.csv')
    print(pokemon_df)
    print(pokemon_df.columns)
    
    # column headers can be used to access individual columns
    print(pokemon_df['Name'])
    print(pokemon_df.HP)
    print(pokemon_df['Type 1'])

    pokemon_df['Attack Ratio'] = pokemon_df['Attack'] / pokemon_df['Sp. Atk']

    print(pokemon_df.head(10))
    print(pokemon_df.sample(3))
    print(pokemon_df.shape)
    print(pokemon_df.info())
    print(pokemon_df.describe())
    print(pokemon_df['Defense'].describe())
    print(pokemon_df['Type 1'].value_counts())
    print(pokemon_df.loc[4])
    print(pokemon_df.groupby('Type 1')[['HP','Speed']].mean())
    print(pokemon_df.groupby('Type 1').size().sort_values(ascending=False))
    pokemon_df['Total'] = pokemon_df[ ['HP','Attack','Defense','Speed'] ].sum(axis=1)
    print(pokemon_df['Total'])
    print(pokemon_df.groupby('Generation')['Total'].mean())

    print(pokemon_df.groupby('Legendary')['Total'].mean())

    subset1 = pokemon_df[(pokemon_df['HP'] > 100)]
    print(subset1)

    subset2 = pokemon_df[(pokemon_df['Type 1'] == 'Psychic')]
    print(subset2)

    subset3 = subset2[(subset2['Type 2'] == 'Fairy') & (subset2['Sp. Atk'] > 50)]
    print(subset3)

    subset4 = pokemon_df[pokemon_df['Name'].str.contains('Mega')]
    print(subset4)

    subset5 = pokemon_df[pokemon_df['Legendary'] == False]
    # shortcut with ~ operator
    subset6 = pokemon_df[~pokemon_df['Legendary']]
    print(subset5)
    print(subset6)


if __name__ == "__main__":
    main()