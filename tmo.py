import os
import glob
from tqdm import tqdm
import numpy as np_img

os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2

# default values
GAMMA = 2.0
INTENSITY = -1.0
LIGHT_ADAPT = 0.8
COLOR_ADAPT = 0.0

hdr4rttRoot = os.path.join(os.getcwd(), 'resources', 'hdr4rtt')
hdrPath = os.path.join(hdr4rttRoot, 'yolo-hdr4rtt', 'images')
tmoHdrPath =  os.path.join(hdr4rttRoot, 'tmo-yolo-hdr4rtt', 'images')

paths = glob.glob(os.path.join(hdrPath, '*'))
for p in tqdm(paths):
    hdr = cv2.imread(p, cv2.IMREAD_UNCHANGED )
    
    op = cv2.createTonemapReinhard(
                gamma=GAMMA,
                intensity=INTENSITY,
                light_adapt=LIGHT_ADAPT,
                color_adapt=COLOR_ADAPT
            )
    tmo_img = op.process(hdr)

    name = p.split('\\')[-1].split('.')[0]
    ext = 'jpg'
    out_name = os.path.join(tmoHdrPath, name+'.'+ext)
    
    cv2.imwrite(out_name, (tmo_img * 255).astype('uint8'))

