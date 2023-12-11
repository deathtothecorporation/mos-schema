import cv2
import os
# iterate through all components and subdirectories and check that all sizes are the same

# path to components
path = "./components"

size = None

# iterate through all components
for componentType in os.listdir(path):
    # iterate through all images
    for componentVariant in os.listdir(path + "/" + componentType):
        # read image
        img = cv2.imread(path + "/" + componentType + "/" + componentVariant)
        # get size of image
        size = img.shape
        # if we haven't set the size yet, set it
        if size is None:
            size = img.shape
        # if the size is not the same, print an error
        if size != img.shape:
            print("Error: " + componentType + "/" + componentVariant + " has a different size than the other images in the directory")
            print("Expected: " + str(size) + ", got: " + str(img.shape))
            exit(1)