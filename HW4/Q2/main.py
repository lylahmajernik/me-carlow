# -*- coding: utf-8 -*-
"""
q2a & q2b
"""

import pandas as pd

df = pd.read_csv("../Data/locations.csv")

dfNaN = (df[df.isnull().any(axis=1)])
dfNaN = dfNaN.fillna(999)
dfNaN.to_csv('q2a.out', na_rep='null')

df2 = pd.read_csv('../Data/regions.csv')

newRegion = dict({'id': 999, 'identifier': "Carlow"})

newdf = pd.DataFrame([newRegion])
combodf = pd.concat([df2,newdf])

combodf.to_csv('q2b.out')