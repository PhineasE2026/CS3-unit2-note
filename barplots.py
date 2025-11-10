import pandas as pd
from matplotlib import pyplot as plt

# Data
languages = {
    'lang': ['Spanish', 'French', 'Mandarin', 'English'],
    'speakers': [5, 2, 2, 8],
    'difficulty': [4, 5, 8, 1],
}

# turn dictionary into dataframe
df = pd.DataFrame(languages)

# Bar charts are great for COUNTS
# often use String data for the labels
df_sorted = df.sort_values(by='speakers', ascending=False)
colors = ['yellow', 'green', 'blue', 'red']
plt.bar(df_sorted['lang'], df_sorted['speakers'], color=colors, width=0.6)
plt.xticks(rotation=45)
plt.xlabel('Language')
plt.ylabel('# of Speakers')
plt.title('Speakers by Language')
plt.savefig('barchart.png', bbox_inches='tight')
plt.close()

# Pie charts — to show parts of a whole/breakdown of a total
plt.pie(df['speakers'], labels=df['lang'].tolist(),startangle=270)
plt.title('Breakdown of Language Speakers')
plt.savefig('piechart.png', bbox_inches='tight')