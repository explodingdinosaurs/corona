import numpy as np
import pandas as pd
import plotly.graph_objects as go
import wikipedia as wp
import re

# Get the data
html = wp.page("2020_coronavirus_pandemic_in_Australia").html().encode("UTF-8")
df = pd.read_html(html)[4]

df = df.rename(columns={'Unnamed: 0': 'date'})
df = df.set_index('date')

# Drop all the rows with NaN index. This cleans up column titles at the
# bottom of the table 
df = df.drop([np.nan])

# Drop reference columns
for state in list(df):
    if state[-2:] == '.1':
        df = df.drop([state], axis=1)
        
# Clean the references from the data
for state in list(df):
    try:
        df[state] = df[state].str.replace(r"\[.*\]","")
    except AttributeError:
        pass

# Clean the references from the column names
for state in list(df):
    try:
        new_state = re.sub("[\(\[].*?[\)\]]", "", state)
        df = df.rename(columns={state: new_state})
    except AttributeError:
        pass

# Drop newcases and % growth
df = df.drop(['Newcases', '%growth'], axis=1)

# Set dtype as float64
df = df.astype('float64')

# Make the dataframe to subtract
# Drop the last row (most recent data) of the df
df_minus_1 = df.drop(df.tail(1).index)

# Drop the first row of the dataframe
df = df.drop(df.head(1).index)

# Lets copy the index
index = df.index

# Drop the index from both
df = df.reset_index(drop=True)
df_minus_1 = df_minus_1.reset_index(drop=True)

# Subtract the two
df = df.subtract(df_minus_1)

# Put the index back in
df.index = index

# Let's plot this mofo    
fig = go.Figure()

# Plot all the states!
for state in list(df):
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df[state],
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='COVID-19 Cases by State/Territory in Austalia',
                   xaxis_title='Date',
                   yaxis_title='Additional Cases')

    
fig.show()

