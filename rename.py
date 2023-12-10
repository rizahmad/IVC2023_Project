import os
import glob
from tqdm import tqdm

hdrRoot = os.path.join(os.getcwd(), 'resources', 'hdr-yolo-coco-person')
hdrTrain = os.path.join(hdrRoot, 'train', 'images')
hdrValidation = os.path.join(hdrRoot, 'validation', 'images')

hdrTrainFilePaths = glob.glob(os.path.join(hdrTrain, '*'))
hdrValidationFilePaths = glob.glob(os.path.join(hdrValidation, '*'))

paths = list()
paths.extend(hdrTrainFilePaths)
paths.extend(hdrValidationFilePaths)

# for p in tqdm(paths):
#     name = p.split('_prediction')[0]
#     ext = p.split('.')[-1]
#     os.rename(p, name+'.'+ext)
