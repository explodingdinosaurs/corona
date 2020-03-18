import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Get the data
data_address = 'https://covid.ourworldindata.org/data/total_cases.csv'

# plot the data
df = pd.read_csv(data_address)
df = df.set_index('date')

df=df[['Australia']]

df[['Australia_log']] = np.log10(df[['Australia']])

df = df.reset_index(drop=True)
y = np.array(df['Australia_log'])
y = y[40:]
x = np.array(df.index)
x = x[:y.shape[0]]

# Fit with polyfit
# log(cases) = a*days + b
# y = a*x + b
a, b = np.polyfit(x, y, 1)
print(f'a: {a}')
print(f'b: {b}')

# Solve for australian population
# (log(cases)-b)/a = x
days = (np.log10(24.6E6) - b)/a
days_until_all_infected = days-x.shape[0]

print(f'entire Australian population infected in {days_until_all_infected} days')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.plot(x,y)
plt.show()
