import numpy as np
import pandas as pd

"""
working with bjects in a list and using pandas
to create a default index for each element

"""

exec = pd.Series([1, 3.5,'some', 'data', 2, 4])
print(exec)

"""
Creating labled columns
"""

date = pd.date_range('20220728', periods=6)
print(date)

col = pd.DataFrame(np.random.randn(6, 4), index=date, columns=list("ABCD"))
print(col)