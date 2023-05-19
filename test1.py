from models import yolo
import torch

model = torch.hub.load('ultralytics/yolov3','yolov3',pretrained=True,channels=3,classes=80)
model1 = yolo.Model("models/yolov3.yaml")model1.load_state_dict(model.state_dict())torch.save(model1.state_dict(),"my_yolov3.pt")
