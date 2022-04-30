#new notebook 

from google.colab import files
data_to_load = files.upload()

#new notebook 

import plotly.express as px
import csv

with open("sm.csv") as csv_files:
  df = csv.DictReader(csv_files)
  fig=px.scatter(df, x="Marks In Percentage", y="Days Present")
  fig.show()

#new notebook 

import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    Average_time_spent = []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_files)
        for row in csv_reader:
            size_of_tv.append(float(row["Marks In Percentage"]))
            Average_time_spent.append(float(row["Days Present"]))

    return {"x" : size_of_tv, "y": Average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks and Days present = ",correlation[0,1])

data_path  = "sm.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)