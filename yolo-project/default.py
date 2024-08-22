import cv2
from PIL import Image

from ultralytics import YOLO

model = YOLO("yolov8n.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True)  # Display preds. Accepts all YOLO predict arguments

# from PIL
im1 = Image.open("{PATH TO IMAGE}")
results = model.predict(source=im1, save=True)  # save plotted images
# results = model.predict(source=im1, save=False)  # do not save plotted images
#results = model.predict(conf=0.5, source=im1, save=True)  # save plotted images
#
# # from ndarray
# im2 = cv2.imread("bus.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels
#
# # from list of PIL/ndarray
# results = model.predict(source=[im1, im2])
