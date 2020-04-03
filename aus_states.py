import numpy as np
import plotly.graph_objects as go
import prepare_data

df_aus = prepare_data.australia()

# Let's plot this mofo    
fig = go.Figure()

# Plot all the states!
for state in list(df_aus):
    fig.add_trace(go.Scatter(
        x=df_aus.index,
        y=df_aus[state],
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='COVID-19 Cases by State/Territory in Austalia',
                   xaxis_title='Date',
                   yaxis_title='Cases')

fig.show()

# Let's plot this log mofo
log_fig = go.Figure()

# Plot all the states!
for state in list(df_aus):
    log_fig.add_trace(go.Scatter(
        x=df_aus.index,
        y=np.log2(df_aus[state].astype('float64')),
        name=state,
    ))

# Make the plot look fancy. 
log_fig.update_layout(title='COVID-19 Cases by State/Territory in Austalia',
                   xaxis_title='Date',
                   yaxis_title='log2(Cases)')

    
log_fig.show()

