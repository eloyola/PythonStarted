import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()
subskey = os.getenv('SUBSCRIPTION_KEY')
print(subskey)

# You need to update the vision_service_address to the address of
# your Computer Vision Service
vision_service_address = "https://pythonimageanalyzerel.cognitiveservices.azure.com/"

# Add the name of the function you want to call to the address
address = vision_service_address + "/vision/v3.0/analyze"

# According to the documentation for the analyze image function 
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color', 'language':'es'}

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subskey}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))