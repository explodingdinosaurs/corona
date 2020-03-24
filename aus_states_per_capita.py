import numpy as np
import pandas as pd
import plotly.graph_objects as go
import wikipedia as wp
import re

# Get the data
html = wp.page("2020_coronavirus_pandemic_in_Australia").html().encode("UTF-8")
df = pd.read_html(html)[6]
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

population = {
    'NSW':8089526,
    'Qld':5095100,
    'Vic':6594804,
    'SA':1751693,
    'WA':2621680,
    'Tas':534281,
    'ACT':426709,
    'NT':245869,
    'Total':25359662,
    'New Cases':25359662, 
}

# Plot all the states!
for state in list(df):
    
    fig.add_trace(go.Scatter(
        x=df.index,
        y=pd.to_numeric(df[state]).divide(population[state])*100000,
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='COVID-19 Cases by State/Territory in Austalia',
                   xaxis_title='Date',
                   yaxis_title='Cases per 100,000 people')

    
fig.show()

