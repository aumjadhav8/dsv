import plotly.express as px
import pandas as pd

# Create a DataFrame with minimal data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'z': [100, 110, 120, 130, 140]
})

fig = px.scatter_3d(df, x='x', y='y', z='z')
fig.show()
