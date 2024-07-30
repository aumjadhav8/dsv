import plotly.express as px
import numpy as np
import datetime

# Generate dates and values
dates = [datetime.datetime(2023, 1, 1) + datetime.timedelta(days=i) for i in range(100)]
values = np.random.randn(100).cumsum()

# Plot the time series
px.line(x=dates, y=values).show()