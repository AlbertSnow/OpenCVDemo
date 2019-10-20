import os
from PIL import Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower
            print(label, path)

            # y_labels.append(label)
            # x_train.append(path) # trun into a NUMPY array, GRAY
            
            pil_image = Image.open(path).convert("L") # grayscale
            image_array = np.array(pil_image, "uint8")
            print(image_array)
