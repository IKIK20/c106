import plotly.express as px
import csv
import numpy as np

with open("icecreamData.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = 'Temperature', y = 'Ice-cream Sales( ₹ )')
    #fig.show()

def getData(data_path):
    icecream_sales = []
    temp = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            icecream_sales.append(float(row['Ice-cream Sales( ₹ )']))
            temp.append(float(row['Temperature']))

    return {'x': temp, 'y': icecream_sales}

def findCorr(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation)

def setup():
    data_path = "icecreamData.csv"
    datasource = getData(data_path)
    findCorr(datasource)

setup()