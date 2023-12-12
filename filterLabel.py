import regex as re
import os
import glob
import shutil

# C:\Users\Maanz-AI\Documents\LUMS\IVC\project\IVC2023_Project\resources\yolo-coco-person\train\labels
inputDir = os.path.join(os.getcwd(),'resources', 'yolo-coco-person', 'train', 'labels')
outputDir =  os.path.join(os.getcwd(),'resources', 'yolo-coco-person', 'train', 'labels_filtered')

if os.path.exists(outputDir):
    shutil.rmtree(outputDir)
os.mkdir(outputDir)

filePaths = glob.glob(os.path.join(inputDir, '*'))

for p in filePaths:
    filename = p.split('\\')[-1]
    f = open(p, 'r')
    text = f.readlines()
    f.close
    matches = list()
    for t in text:
        matches.extend(re.findall('(0 (.*))', t))
    for m in matches:
        f = open(os.path.join(outputDir, filename), 'w')
        f.write(m)
    
