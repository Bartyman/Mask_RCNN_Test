import os
import json
from shutil import copyfile
import glob
from jsonmerge import merge

JSON_DIR = os.path.abspath("C:/Users/todd_/OneDrive/sub_images/Annotation files for training")
SRC_DIR = os.path.abspath("C:/Users/todd_/Documents/Data science/Data Science Project 1/Images/resize")
DEST_DIR = os.path.abspath("C:/Users/todd_/OneDrive/sub_images/Annotation files for training/mixed")

annotations1 = json.load(open(os.path.join(JSON_DIR, "Mixed_4Dec2020_1h33m.json")))  # "via_region_data.json")))
annotations = list(annotations1.values())  # don't need the dict keys

# annotations. Skip unannotated images.
annotations = [a for a in annotations if a['regions']]

# Copy images
for a in annotations:
    print(a['filename'])
    copyfile(os.path.join(SRC_DIR, a['filename']), os.path.join(DEST_DIR, a['filename']))