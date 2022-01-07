# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px

url = 'https://github.com/AlexMcClung/World-University-Rankings/raw/master/data/timesData.csv'

df = pd.read_csv(url, engine = 'python')

df['year'].value_counts()

df.query("year == 2016").head()

df['Rank'] = df.world_rank.str.extract('(\d+)').astype(int)

hpy = df[df['university_name'].isin(['Yale University','Princeton University', 'Harvard University'])]

fig = px.line(hpy, x = "year", y = "Rank", color='university_name')

fig.update_yaxes(autorange="reversed")

fig.show()

