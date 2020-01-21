# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:52:30 2019

@author: ANONYME
"""
import pandas as pd 

d ={"a":23,"b":15,"c":48}

pd.Series(d)

pd.Series(list(d.values()),list(d.keys()))

