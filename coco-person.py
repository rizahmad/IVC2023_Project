#https://stackoverflow.com/questions/51100191/how-can-i-download-a-specific-part-of-coco-dataset
import fiftyone.zoo as foz


# Download 1000 Train set images of 'person' class from COCO dataset
dataset = foz.load_zoo_dataset(
    "coco-2017",
    splits=["train", "validation"],
    label_types=["detections"],
    dataset_name="coco-person",
    dataset_dir="./resources/coco-person",
    classes=["person"],
    max_samples=1000,
)

