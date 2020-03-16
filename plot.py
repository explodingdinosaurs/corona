import pandas as pd
import plotly.graph_objects as go

# Get the data
data_address = 'https://covid.ourworldindata.org/data/total_cases.csv'

# plot the data
df = pd.read_csv(data_address)
df = df.set_index('date')

fig = go.Figure()

for country in list(df):
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df[country],
        name=country,
    ))

# Make the plot look fancy. 
fig.update_layout(title='COVID-19 Cases',
                   xaxis_title='Date',
                   yaxis_title='Cases')

    
fig.show()
