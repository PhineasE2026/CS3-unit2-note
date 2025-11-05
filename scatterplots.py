import pandas as pd
from matplotlib import pyplot as plt

cities = pd.read_csv('california_cities.csv')
print(cities.info())

# Extract data columns for our scatterplot
latitudes = cities['latd'] # y values
longitudes = cities['longd'] # x values
populations = cities['population_total']
area = cities['area_total_sq_mi']

# gen scatter
plt.scatter(longitudes, latitudes)
plt.savefig('scatter-cities.png')
plt.close()