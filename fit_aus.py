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
b, m = np.polyfit(x, y, 1)
print(f'b: {b}')
print(f'm: {m}')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.plot(x,y)
plt.show()

## Plot the data
#fig = go.Figure()
#
#for country in list(df_gt_100):
#    fig.add_trace(go.Scatter(
#        x=df_gt_100.index,
#        y=np.log10(df_gt_100[country]),
#        name=country,
#    ))
#
#fig.show()
