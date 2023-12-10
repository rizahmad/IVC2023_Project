# local setup commands
git clone https://github.com/rizahmad/IVC2023_Project.git
cd IVC2023_Project
git submodule update --init

# for dataset handling, read script files first
python -m venv .\venv
.\venv\Scripts\activate.bat
python pip install -r requirements.txt
python coco-person.py
python yolo.py
deactivate

# for running yolo
cd yolo
python -m venv .\venv
.\venv\Scripts\activate.bat
python pip install -r requirements.txt

deactivate
