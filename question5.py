import pandas as pd
df = pd.read_csv('country_vaccination_stats.csv')
df = df.fillna(0)
clistdf = df.groupby(['country'])['daily_vaccinations'].median().reset_index()
print(clistdf.nlargest(3,'daily_vaccinations'))
