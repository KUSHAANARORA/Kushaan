import pandas as pd
import plotly_express as px
# df = pd.read_csv("line_chart.csv")
# fig = px.line(df,x="Year",y="Per capita income",color="Country",title="Per capita income")
# fig.show()
df1 = pd.read_csv("data.csv")
fig = px.bar(df1,x = "Country",y="population",color="Green")
fig.show()