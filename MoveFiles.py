import os
import json
import glob
from jsonmerge import merge

DATASET_DIR = os.path.abspath("./Mask_RCNN/dataset")

# result = []
# for f in glob.glob(os.path.join(DATASET_DIR,"*.json")):
#     with open(f, "rb") as infile:
#         result.append(json.load(infile))
#         #print(result)
# #print(result)
# with open(os.path.join(DATASET_DIR,"merged_file.json"), "w") as outfile:
#      json.dump(result, outfile)
result = ""
for f in glob.glob(os.path.join(DATASET_DIR,"*.json")):
    with open(f, "rb") as infile:
        jsonFile = json.load(infile)
        if result == "":
            result = jsonFile
        else:
            result = merge(result, jsonFile)
        #print(result)

with open(os.path.join(DATASET_DIR,"merged_file.json"), "w") as outfile:
     json.dump(result, outfile)

#test = json.load(open(os.path.join(DATASET_DIR, "wood_29Nov_11h49m.json")))
#test = json.load(open(os.path.join("./Mask_RCNN/dataset", "Brick_30Nov_22h30m.json")))
#test = json.load(open(os.path.join("./Mask_RCNN/dataset", "Soil_30Nov_22h20m.json")))
test = json.load(open(os.path.join(DATASET_DIR, "merged_file.json")))
print(test)
test2 = list(test.values())

test2 = [a for a in test2 if a['regions']]
count= 0
for a in test2:
    count +=1
    print(a['filename'])
print(count)