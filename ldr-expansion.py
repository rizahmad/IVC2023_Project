import glob
import os
import sys
import argparse
import torch

sys.path.append(os.path.join(os.getcwd(),'hdr-expandnet'))
from expand import create_images
import util

from util import (
    process_path,
    split_path,
    map_range,
    str2bool,
    cv2torch,
    torch2cv,
    resize,
    tone_map,
    create_tmo_param_from_args,
)


def create_args():
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('ldr', nargs='+', type=process_path, help='Ldr image(s)')
    arg(
        '--out',
        type=lambda x: process_path(x, True),
        default=None,
        help='Output location.',
    )
    arg(
        '--video',
        type=str2bool,
        default=False,
        help='Whether input is a video.',
    )
    arg(
        '--patch_size',
        type=int,
        default=256,
        help='Patch size (to limit memory use).',
    )
    arg('--resize', type=str2bool, default=False, help='Use resized input.')
    arg(
        '--use_exr',
        type=str2bool,
        default=False,
        help='Produce .EXR instead of .HDR files.',
    )
    arg('--width', type=int, default=960, help='Image width resizing.')
    arg('--height', type=int, default=540, help='Image height resizing.')
    arg('--tag', default=None, help='Tag for outputs.')
    arg(
        '--use_gpu',
        type=str2bool,
        default=torch.cuda.is_available(),
        help='Use GPU for prediction.',
    )
    arg(
        '--tone_map',
        choices=['exposure', 'reinhard', 'mantiuk', 'drago', 'durand'],
        default=None,
        help='Tone Map resulting HDR image.',
    )
    arg(
        '--stops',
        type=float,
        default=0.0,
        help='Stops (loosely defined here) for exposure tone mapping.',
    )
    arg(
        '--gamma',
        type=float,
        default=1.0,
        help='Gamma curve value (if tone mapping).',
    )
    arg(
        '--use_weights',
        type=process_path,
        default='weights.pth',
        help='Weights to use for prediction',
    )
    arg(
        '--ldr_extensions',
        nargs='+',
        type=str,
        default=['.jpg', '.jpeg', '.tiff', '.bmp', '.png'],
        help='Allowed LDR image extensions',
    )
    

    ldrRoot= os.path.join(os.getcwd(), 'resources', 'yolo-coco-person')
    ldrTrain = os.path.join(ldrRoot, 'train', 'images')
    ldrValidation = os.path.join(ldrRoot, 'validation', 'images')

    hdrRoot = os.path.join(os.getcwd(), 'resources', 'hdr-yolo-coco-person')
    hdrTrain = os.path.join(hdrRoot, 'train', 'images')
    hdrValidation = os.path.join(hdrRoot, 'train', 'validation')

    weightsPath = os.path.join('hdr-expandnet', 'weights.pth')
    opt = parser.parse_args([ldrTrain, '--out',hdrTrain, '--use_weights', weightsPath])

    return opt

create_images(create_args())

# python_file_path = "/content/drive/MyDrive/IVC23/drive/hdr-expandnet-master/expand.py"
# ldr_input_path = "/content/drive/MyDrive/IVC23/drive/VOC/train/VOC2012_train_val/JPEGImages"
# hdr_out_path = "/content/drive/MyDrive/IVC23/drive/Generated_HDR"
# !python "{python_file_path}" "{ldr_input_path}" --out "{hdr_out_path}"


