# -*- coding: utf-8 -*-
"""
q3
"""

import pandas as pd

df = pd.read_csv("../Data/pokemon.csv")

vowels = ('a','e','i','o','u')


dfVowel = df[df['identifier'].str.startswith(vowels)]


dfVowel.to_csv('q3.out')