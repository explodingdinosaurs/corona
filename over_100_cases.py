import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Get the data
data_address = 'https://covid.ourworldindata.org/data/total_cases.csv'

# plot the data
df = pd.read_csv(data_address)
df = df.set_index('date')

# Find all entries greater than 100
df_100_bool = df > 100

# Set entries < 100 to 0
df_gt_100 = df * df_100_bool

# Remove date index
df_gt_100 = df_gt_100.reset_index(drop=True)

# Replace zeros with NaNs
df_gt_100 = df_gt_100.replace({0:np.nan})

# Remove countries with all NaN entries
df_gt_100 = df_gt_100.dropna(axis='columns', how='all')

# Shift values up
df_gt_100 = df_gt_100.apply(lambda x: pd.Series(x.dropna().values))
                              
# Plot the data
fig = go.Figure()

for country in list(df_gt_100):
    fig.add_trace(go.Scatter(
        x=df_gt_100.index,
        y=df_gt_100[country],
        name=country,
    ))

# Make the plot look fancy. 
fig.update_layout(title='COVID-19 Cases from First Day Above 100 Cases',
                   xaxis_title='Day Number',
                   yaxis_title='Cases')
    
fig.show()
