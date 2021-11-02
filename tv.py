import plotly.express as px
import csv
import numpy as np

def getData(data_path):
    tv_size = []
    time = []

    with open(data_path) as f:
        df= csv.DictReader (f)
        for row in df:
            tv_size.append(float(row["Size of TV"]))
            time.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    
    return {'x': time, 'y': tv_size}

def findCorr(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation)

def setup():
    data_path = "tv.csv"
    datasource = getData(data_path)
    findCorr(datasource)

setup()

        

