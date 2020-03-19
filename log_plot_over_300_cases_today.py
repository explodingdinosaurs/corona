"""Plot only log2 for Countries that have over 300 cases today.

Linear behaviour indicated exponential growth
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot #I added offline plot  

# Threshold number of cases to plot that country
Tresh_Cases = 300

# Get the data
data_address = 'https://covid.ourworldindata.org/data/total_cases.csv'
df = pd.read_csv(data_address)
df = df.set_index('date')

#Select only Countries that have more than Tresh_Cases cases today
more_than_100_today = (df[:][-1:] > Tresh_Cases)
df_relevant = df[df.columns[more_than_100_today.iloc[0,:]]]

#----  Periods with less than 30 cases are ignored ----
df_30_bool = df_relevant > 30
# Set entries < 30 to 0
df_relevant = df_relevant * df_30_bool
# Set entry of 0 to NaN - stops divide by 0 errors
df_relevant = df_relevant.replace({0:np.nan})

# Remove date index
df_relevant = df_relevant.reset_index(drop=True)

# Drop the International data.. is it cruise ships???
df_relevant = df_relevant.drop(['International'], axis=1)

# Plot the data
fig = go.Figure()

for country in list(df_relevant):
    fig.add_trace(go.Scatter(
        x=df_relevant.index,
        y=np.log2(df_relevant[country]),
        name=country,
    ))

# Make the plot look fancy. 
fig.update_layout(title='SARS-CoV-2 Cases in Logarithmic scale: Linear behaviour indicates exponential growth',
                   xaxis_title='Day Number',
                   yaxis_title='Log2(Cases)')
    
fig.show()

