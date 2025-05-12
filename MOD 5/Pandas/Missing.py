import pandas as pd
import numpy as np

# Create a DataFrame with NaN values
data = {
    'Year': [2010, 2011, 2013, 2014, 2015],
    'Revenue': [100, 120, np.nan, 140, 150]
}

df = pd.DataFrame(data)

print("Before Interpolation:")
print(df)

# Interpolate missing Revenue values using linear interpolation
df['Revenue'] = df['Revenue'].interpolate(method='linear')

print("\nAfter Interpolation:")
print(df)
