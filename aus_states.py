import numpy as np
import pandas as pd
import plotly.graph_objects as go
import wikipedia as wp
import re

# Get the data
html = wp.page("2020_coronavirus_pandemic_in_Australia").html().encode("UTF-8")
df = pd.read_html(html)[6]
print(df)
df = df.rename(columns={'Unnamed: 0': 'date'})
df = df.set_index('date')

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
                   yaxis_title='Cases')

    
fig.show()

