import requests
import dotenv
import os
import time

dotenv.load_dotenv()
pixel_endpoint = "https://pixe.la/v1/users/"
USER = os.environ['USERNAME']
TOKEN = os.environ['TOKEN']


# graph_endpoint = f"https://pixe.la/v1/users/{os.environ['USERNAME']}/graphs"
# graph_params = {
#     "id":"graph1",
#     "name":"Coding Graph",
#     "unit":"commit",
#     "type":"int",
#     "color":"ajisai"
# }
#
# headers = {
#     "X-USER-TOKEN":os.environ["TOKEN"]
# }
# response = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
# print(response.text)

today = time.strftime('%Y%m%d')
# print(today)
#
# post_pixel_endpoint = f"https://pixe.la/v1/users/{USER}/graphs/graph1"
# post_pixel_params = {
#     "date":today,
#     "quantity":"1"
# }
headers ={
    "X-USER-TOKEN":TOKEN
}
#
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)

# put_pixel_endpoint = f"{pixel_endpoint}{USER}/graphs/graph1/{today}"
# params = {
#     "quantity":"4"
# }
#
# response = requests.put(url=put_pixel_endpoint, json=params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixel_endpoint}{USER}/graphs/graph1/{today}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)

