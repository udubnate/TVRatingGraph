# Installed with pip3 install plotly==4.13.0

import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()