import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Data/Data.csv')


df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)



# Creating medal columns
df['DoorDash'] = df['DoorDash']
df['UberEats'] = df['UberEats']
df['PostMates'] = df['PostMates']
df['GrubHub'] = df['GrubHub']

# Preparing data
trace1 = go.Bar(x=df['Restaurant'], y=df['DoorDash'], name='DoorDash', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=df['Restaurant'], y=df['UberEats'], name='UberEats', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=df['Restaurant'], y=df['PostMates'], name='PostMates', marker={'color': '#FFD700'})
trace3 = go.Bar(x=df['Restaurant'], y=df['GrubHub'], name='GrubHub', marker={'color': '#FF0000'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Which Restaurants use Delivery Services', xaxis_title="Restaurants",
                   yaxis_title="Wait Time", barmode='stack')
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')