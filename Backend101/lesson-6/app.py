import numpy as np
import requests

response = requests.get("https://onleadify.com/")
print(f"Data of API {response}")
array = np.array([1,2,3,4,5])
print(array)