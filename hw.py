import pandas as pd
import plotly.express as px
df=pd.read_csv("HWdata.csv")
bargraph=px.scatter(df,x='date',y='cases', color='country')
bargraph.show()