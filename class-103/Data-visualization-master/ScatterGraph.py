import pandas as pd
import plotly.express as ps

df = pd.read_csv("C:\Projects\class-103\Data-visualization-master\csv files\data.csv")
figure = ps.scatter(df, x="Population", y="Per capita", size="Percentage", color="Country")
figure.show()