# IVC-2023 Project repository
## Group members
|Name | Contact |
|Rizwan Ahmad Bhatti | 21030005@lums.edu.pk |
|Muhammad Saad | 24100012@lums.edu.pk |

## Directory structure
Repository consists of some external repositories added as git submodules.
```
IVC2023_Project/
├─ HDR_YOLOv7/
├─ hdr_expandnet/
├─ JSON2YOLO/
├─ yolov7/
├─ resources/
checkcuda.py
coco-person.py
ldr-expansion.py
rename.py
requirements.txt
tmo.py
yolo.py
readme.md
```
### checkcuda.py
Used to check if cuda support is present. If not then cuda has to be installed.

### coco-person.py
Used to download 1000 images for train and validation set from MS COCO repository for person category.

### ldr-expansion.py
Used to convert ldr images to hdr images using the ExpandNet pretrained model.

### rename.py
Utility script to rename files.

### requirements.txt
Used to collect requirements for the python environment

### tmo.py
Used to convert hdr from HDR4RTT repository to LDR images.

### yolo.py
Used to convert MS COCO JSON format to YOLO annotations format using the JSON2YOLO repository.

### readme.md
This file.

## Experiment setup
### Clone IVC2023_Project
```
git clone https://github.com/rizahmad/IVC2023_Project.git
cd IVC2023_Project
git submodule update --init
```
### Copy resources folder
resources folder must be copied into the yolov7 and HDR_YOLOv7 repository folders since it contains the dataset required.

### Create python environment
#### LDR pipeline
```
cd yolov7
python -m venv .\venv
.\venv\Scripts\activate.bat
python pip install -r requirements.txt
pip uninstall torch torchvision
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121
python train.py --noautoanchor --cfg resources\yolo-coco-person\yaml\cfg.yaml --data resources\yolo-coco-person\yaml\data.yaml --epochs 300 --weights '' --img-size 320 320
python detect.py --weights runs\train\exp4\weights\epoch_099.pt --source resources\hdr4rtt\tmo-yolo-hdr4rtt\images --img-size 320
```
#### HDR pipeline
```
cd HDR_YOLOv7
python -m venv .\venv
.\venv\Scripts\activate.bat
set OPENCV_IO_ENABLE_OPENEXR=1
python pip install -r requirements.txt
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121
python train.py --noautoanchor --cfg resources\hdr-yolo-coco-person\yaml\cfg.yaml --data resources\hdr-yolo-coco-person\yaml\data.yaml --epochs 300 --weights '' --img-size 320 320
python detect.py --weights runs\train\exp\weights\epoch_099.pt --source resources\hdr4rtt\yolo-hdr4rtt\images --img-size 320
```
