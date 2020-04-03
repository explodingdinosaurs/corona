import pandas as pd
import plotly.graph_objects as go
import prepare_data

population = {
    'NSW':8089526,
    'QLD':5095100,
    'VIC':6594804,
    'SA':1751693,
    'WA':2621680,
    'TAS':534281,
    'ACT':426709,
    'NT':245869,
    'Total':25359662,
    'DeathsNationally':25359662,
}

df_aus = prepare_data.australia()
df_aus_change = prepare_data.australia_change(df_aus)

# Let's plot this mofo    
fig = go.Figure()

# Plot all the states!
for state in list(df_aus):
    fig.add_trace(go.Scatter(
        x=df_aus.index,
        y=pd.to_numeric(df_aus[state]).divide(population[state])*100000,
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='Per Capita COVID-19 Cases by State/Territory in Austalia',
                   xaxis_title='Date',
                   yaxis_title='Cases per 100,000 people')
fig.show()

# Let's plot this mofo
fig_change = go.Figure()

# Plot all the states!
for state in list(df_aus_change):
    fig_change.add_trace(go.Scatter(
        x=df_aus_change.index,
        y=pd.to_numeric(df_aus_change[state]).divide(population[state])*100000,
        name=state,
    ))

# Make the plot look fancy.
fig_change.update_layout(title='Per Capita Change in COVID-19 Cases by State/Territory in Austalia',
                         xaxis_title='Date',
                         yaxis_title='Change in cases per 100,000 people')
fig_change.show()


# Roll those numbers over a week
df_aus_change = df_aus_change.rolling(7).mean()

# Let's plot this mofo
fig_rolling_change = go.Figure()

# Plot all the states!
for state in list(df_aus):
    fig_rolling_change.add_trace(go.Scatter(
        x=df_aus_change.index,
        y=pd.to_numeric(df_aus_change[state]).divide(population[state])*100000,
        name=state,
    ))

# Make the plot look fancy.
fig_rolling_change.update_layout(
    title='7-day Rolling Per Capita Change in COVID-19 Cases by State/Territory in Austalia',
    xaxis_title='Date',
    yaxis_title='Change in cases per 100,000 people'
)

fig_rolling_change.show()
