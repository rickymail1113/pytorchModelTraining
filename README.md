# pytorchModelTraining

1. install opencv-python
2. pip3 install torch torchvision torchaudio
3. 新增兩個目錄 data/images     data/labels
4. git clone https://github.com/tzutalin/labelimg
5. git clone https://github.com/ultralytics/yolov5
6. cd .\yolov5\
7. pip install -r .\requirements.txt
8. python -m pip install msvc-runtime  
9. restart PyCharm
10. install PyQt5
11. install lxml
12. cd .\labelimg
13. 終端機虛擬環境下執行 pyrcc5 -o lib/resource.py resources.qrc
14. labelimg/data/predefined_classes.txt 修改為自己要辨識的例如 
nomask
mask
15. python labelimg.py
16. 定義自己的照片&選擇yolo格式
17. 在yolov5目錄新增dataset.yaml檔案 (做了一份在專案跟目錄下,複製過去即可)
18. 終端機虛擬環境切換至 yolov5
19. 開始訓練 python train.py --img 320 -batch 16 --epoch 10 --data dataset.yaml --weight yolov5s.pt
(更改訓練次數 --epoch N, 更改訓練模型精度 --weight yolov5N.pt)
20. 等待訓練結束
21. 執行phoneDetection.py 
(修改為自己訓練的 expN)
path='./yolov5/runs/train/exp2/weights/best.pt'