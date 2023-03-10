from fastapi import FastAPI
from fastapi.responses import*
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()

@app.get("/iris-plot")

def plot():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    plt.scatter(iris['sepal_length'],iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png',mode="rb")

    return StreamingResponse(file,media_type="image/png")