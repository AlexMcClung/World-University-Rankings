# -*- coding: utf-8 -*-
"""
Load Times Rankings Data

"""

import pandas as pd

url = 'https://github.com/AlexMcClung/World-University-Rankings/raw/master/data/timesData.csv'

df = pd.read_csv(url, engine = 'python')

df['year'].value_counts()

