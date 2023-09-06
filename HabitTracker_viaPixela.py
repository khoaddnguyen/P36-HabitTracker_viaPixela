import requests
from requests import Response
from datetime import datetime

# STEP 1: Create user account
TOKEN = "TOKEN"  # make up a token
USERNAME = "USERNAME"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # call STEP 1 here
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP 2: Create a graph definition

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

# Request header as the authenticated token

headers = {
    "X-USER-TOKEN": TOKEN
}

# # call STEP 2 here
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# STEP 3: Get the graph by browsing https://pixe.la/v1/users/(ADD USERNAME HERE)/graphs/(ADD GRAPH_ID HERE).html

# STEP 4: Add value to graph

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=7, day=22)  # format yyyy-mm-dd

pixel_data = {
    "date": today.strftime("%Y%m%d"),  # format yyyymmdd,
    "quantity": input("How many kilometers did you run today? ")
}

# # call STEP 4 here
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# STEP 5: Update a pixel

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}
# # call STEP 5 here
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# STEP 6: Delete a pixel

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# # call STEP 6 here
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)