import pandas as pd
import plotly.express as ps

df = pd.read_csv("C:\Projects\class-103\Data-visualization-master\csv files\data.csv")
figure = ps.bar(df, x = "Country", y = "InternetUsers", color = "Country", title = "Per Capita Income")
figure.show()