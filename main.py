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



if __name__ == "__main__":
    main()
