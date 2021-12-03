import pandas as pd
import plotly.express as ps

df = pd.read_csv("C:\Projects\class-103\Data-visualization-master\csv files\line_chart.csv")
figure = ps.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")
figure.show()