import torch
#from PIL import Image
model = torch.hub.load('ultralytics/yolov3', 'yolov3')

# Images
img = './data/images/person_001.jpg'

# Inference
results = model(img)

# Results
results.print()
results.show()
