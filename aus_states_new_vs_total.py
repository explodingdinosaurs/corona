import numpy as np
import plotly.graph_objects as go
import prepare_data

df_aus = prepare_data.australia()
df_aus_change = prepare_data.australia_change(df_aus)

# Gotta drop the first row in df as well so it aligns with df_change
df_aus = df_aus.drop(df_aus.head(1).index)

# Let's plot this mofo    
fig = go.Figure()

# Plot all the states!
for state in list(df_aus):
    fig.add_trace(go.Scatter(
        x=np.log10(df_aus[state]),
        y=np.log10(df_aus_change[state]),
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='Raw Growth vs Cases of Covid-19 in Australia',
                   xaxis_title='log10(Cases)',
                   yaxis_title='log10(New Cases)')
    
fig.show()

# Roll those numbers over a week
df_aus = df_aus.rolling(7).mean()
df_aus_change = df_aus_change.rolling(7).mean()

# Let's plot this mofo    
rolling_fig = go.Figure()

# Plot all the states!
for state in list(df_aus):
    rolling_fig.add_trace(go.Scatter(
        x=np.log10(df_aus[state]),
        y=np.log10(df_aus_change[state]),
        name=state,
    ))

# Make the plot look fancy. 
rolling_fig.update_layout(title='7-day Rolling Mean of Growth vs Cases of Covid-19 in Australia',
                   xaxis_title='log10(Cases)',
                   yaxis_title='log10(New Cases)')
    
rolling_fig.show()

