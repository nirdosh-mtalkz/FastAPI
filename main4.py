import requests
from PIL import Image
import matplotlib.pyplot as plt
import io

response = requests.get('http://127.0.0.1:8000/iris-plot')
file = io.BytesIO(response.content)
im = Image.open(file)
im.show()