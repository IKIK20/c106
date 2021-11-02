import plotly.express as px
import csv

with open("coffee.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, y = 'sleep in hours', x = 'Coffee in ml')
    fig.show()