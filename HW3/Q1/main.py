# -*- coding: utf-8 -*-
"""
Q1
Lylah Majernik
HW3
"""

import pandas as pd

users = [
    ['Abe', 100],
 ['Ben', 90],
 ['Cam', 80],
 ['Dan', 70],
 ['Edd', 60],
 ['Fae', 50],
 ['Gus', 40],
 ['Han', 30],
 ['Ian', 20],
 ['Jan', 10]
]

df = pd.DataFrame(users, columns =['Name', 'Score'])

names = df["Name"]

print(names)


