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