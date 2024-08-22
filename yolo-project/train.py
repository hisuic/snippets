# https://docs.ultralytics.com/modes/train/#key-features-of-train-mode for more information

from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data='{PATH TO data.yaml}', 
    epochs=3, 
    imgsz=640, 
    device='cpu' # Use CPU for training (Option for windows which doesn't have GPU)
)
