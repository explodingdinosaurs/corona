import plotly.graph_objects as go
import prepare_data

df_aus = prepare_data.australia()
df_aus_change = prepare_data.australia_change(df_aus)

# Let's plot this mofo    
fig = go.Figure()

# Plot all the states!
for state in list(df_aus_change):
    fig.add_trace(go.Scatter(
        x=df_aus_change.index,
        y=df_aus_change[state],
        name=state,
    ))

# Make the plot look fancy. 
fig.update_layout(title='COVID-19 Cases by State/Territory in Austalia',
                   xaxis_title='Date',
                   yaxis_title='Additional Cases')

    
fig.show()

