import pandas as pd
df = pd.read_csv('country_vaccination_stats.csv')
clistdf = df.groupby(['country'])['daily_vaccinations'].min().reset_index()
clistdf = clistdf.fillna(0)
df2 = pd.DataFrame()
for i in clistdf['country']:
    minimum = int(clistdf[clistdf["country"] == i]['daily_vaccinations'])
    print(minimum)
#    print(df[['country', 'daily_vaccinations']])
    df2 = df2.append(df[df["country"] == i].fillna(minimum))
print(df2[['country', 'daily_vaccinations']])
df = df.empty
