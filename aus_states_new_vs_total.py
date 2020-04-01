import numpy as np
import pandas as pd
import plotly.graph_objects as go
import wikipedia as wp
import re

# Get the data
html = wp.page("2020_coronavirus_pandemic_in_Australia").html().encode("UTF-8")
df = pd.read_html(html)[5]
df = df.rename(columns={'Unnamed: 0': 'date'})
df = df.set_index('date')


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

# Set everything in the dataframe to float64
df = df.astype('float64')

# Make the dataframe to subtract
# Drop the last row (most recent data) of the df
df_minus_tail = df.drop(df.tail(1).index)

# Drop the first row of the dataframe
df_minus_head = df.drop(df.head(1).index)
index = df_minus_head.index

# Drop the index from both
df_minus_head = df_minus_head.reset_index(drop=True)
df_minus_tail = df_minus_tail.reset_index(drop=True)

# Subtract the two
df_change = df_minus_head.subtract(df_minus_tail)

# Put the index back in
df_change.index = index

# Gotta drop the first row in df as well so it aligns with df_change
df = df.drop(df.head(1).index)

# Let's plot this mofo    
fig = go.Figure()

# Plot all the states!
for state in list(df):
    fig.add_trace(go.Scatter(
        x=np.log10(df[state]),
        y=np.log10(df_change[state]),
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='Raw Growth vs Cases of Covid-19 in Australia',
                   xaxis_title='log10(Cases)',
                   yaxis_title='log10(New Cases)')
    
fig.show()

# Roll those numbers over a week
df = df.rolling(7).mean()
df_change = df_change.rolling(7).mean()


# Let's plot this mofo    
rolling_fig = go.Figure()

# Plot all the states!
for state in list(df):
    rolling_fig.add_trace(go.Scatter(
        x=np.log10(df[state]),
        y=np.log10(df_change[state]),
        name=state,
    ))

# Make the plot look fancy. 
rolling_fig.update_layout(title='7-day Rolling Mean of Growth vs Cases of Covid-19 in Australia',
                   xaxis_title='log10(Cases)',
                   yaxis_title='log10(New Cases)')
    
rolling_fig.show()
