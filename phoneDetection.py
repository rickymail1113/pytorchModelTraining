import cv2
import numpy as np
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5/runs/train/exp4/weights/best.pt', force_reload=True)

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

cap = cv2.VideoCapture(0)
while cap.isOpened():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success, image = cap.read()
    if not success:
        continue

    # image = cv2.resize(image, (640, 480))
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model(image1)
    print(results)
    print(np.array(results.render()).shape)

    image2 = cv2.cvtColor(np.squeeze(results.render()), cv2.COLOR_RGB2BGR)
    cv2.imshow('Train Model', image2)


cap.release()
cv2.destroyAllWindows()

