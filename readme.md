# local setup commands
```
git clone https://github.com/rizahmad/IVC2023_Project.git
cd IVC2023_Project
git submodule update --init
```

# for dataset handling, read script files first
```
python -m venv .\venv
.\venv\Scripts\activate.bat
python pip install -r requirements.txt
python coco-person.py
python yolo.py
deactivate
```

# for running yolo
```
cd yolo
python -m venv .\venv
.\venv\Scripts\activate.bat
python pip install -r requirements.txt

deactivate
```
# for cuda on laptop
```
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121
```

# opencv with hdr images
hdr images require an enironment variable when training with HDR_YOLOv7
```
set OPENCV_IO_ENABLE_OPENEXR=1
```

# hdr training commands
```
set OPENCV_IO_ENABLE_OPENEXR=1
python train.py --noautoanchor --cfg resources\hdr-yolo-coco-person\yaml\cfg.yaml --data resources\hdr-yolo-coco-person\yaml\data.yaml --epochs 300 --weights '' --img-size 320 320
```

# ldr training command
```
python train.py --noautoanchor --cfg resources\yolo-coco-person\yaml\cfg.yaml --data resources\yolo-coco-person\yaml\data.yaml --epochs 300 --weights '' --img-size 320 320
```

# hdr detection command
```
set OPENCV_IO_ENABLE_OPENEXR=1
python detect.py --weights runs\train\exp\weights\epoch_099.pt --source resources\hdr4rtt\yolo-hdr4rtt\images --img-size 320
```

# ldr detection command
```
python detect.py --weights runs\train\exp4\weights\epoch_099.pt --source resources\hdr4rtt\tmo-yolo-hdr4rtt\images --img-size 320
```