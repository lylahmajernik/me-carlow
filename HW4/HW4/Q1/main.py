# -*- coding: utf-8 -*-
"""
q1
"""

import pandas as pd

df = pd.read_csv("../Data/locations.csv")

dfNaN = (df[df.isnull().any(axis=1)])
dfNaN.to_csv('q1.out', na_rep='null')

