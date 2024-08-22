# https://docs.ultralytics.com/modes/train/#key-features-of-train-mode for more information

from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data='./data.yaml', 
    epochs=3, 
    imgsz=640, 
    device='cpu' # using CPU for training (option for windows)
)
