# <snippet_imports>
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticates credentials and creates a client.
'''

subscription_key = "your key"
endpoint = "Your Endpoint"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
END - Authenticate
'''

import cv2

videoCaptureObject = cv2.VideoCapture(0)
try:
    while(True):

        ret,frame = videoCaptureObject.read()
        cv2.imshow('CapturingVideo', frame)
        cv2.imwrite("resources/NewPicture.jpg", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
except Exception:
    pass


print("===== Batch Read File - local =====")
# Get image of handwriting
local_image_handwritten_path = "resources\\NewPicture.jpg"
# Open the image
local_image_handwritten = open(local_image_handwritten_path, "rb")

# Call API with image and raw response (allows you to get the operation location)

recognize_handwriting_results = computervision_client.read_in_stream(local_image_handwritten, raw=True)
# Get the operation location (URL with ID as last appendage)
operation_location_local = recognize_handwriting_results.headers["Operation-Location"]
# Take the ID off and use to get results
operation_id_local = operation_location_local.split("/")[-1]

# Call the "GET" API and wait for the retrieval of the results
while True:
    recognize_handwriting_result = computervision_client.get_read_result(operation_id_local)
    if recognize_handwriting_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print results, line by line
if recognize_handwriting_result.status == OperationStatusCodes.succeeded:
    for text_result in recognize_handwriting_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)

print()