#https://stackoverflow.com/questions/51100191/how-can-i-download-a-specific-part-of-coco-dataset

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'JSON2YOLO'))
from general_json2yolo import convert_coco_json

srcRoot = os.path.join(os.getcwd(),'resources', 'coco-person')
dstRoot = os.path.join(os.getcwd(),'resources', 'yolo-coco-person')

srcTrain = os.path.join(srcRoot, 'train')
srcVal = os.path.join(srcRoot, 'validation')

dstTrain = os.path.join(dstRoot, 'train')
dstVal = os.path.join(dstRoot, 'validation')

# convert_coco_json(srcTrain,  # directory with *.json
#                           use_segments=True,
#                           cls91to80=True)

# convert_coco_json(srcVal,  # directory with *.json
#                           use_segments=True,
#                           cls91to80=True)