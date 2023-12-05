import os
import json
from pprint import pprint

components = []

# scan components/ to get the list of directories
for componentType in os.listdir("./components"):
    # skip non-directories
    if not os.path.isdir(f"./components/{componentType}"):
        continue

    # scan components/<componentType>/ to get the list of files
    for componentVariant in os.listdir(f"./components/{componentType}"):
        # skip non-files
        if not os.path.isfile(f"./components/{componentType}/{componentVariant}"):
            continue

        # add to list of components after removing the file extension
        components.append((componentType, componentVariant.split(".")[0]))

accessories = []
staticComponents = []

for component in components:
    (componentType, componentVariant) = component
    if componentType in ["Background", "Blush", "Eyebrow", "Eyes", "Eye Color", "Hair", "Mouth", "Neck", "Race", "Face Tattoo"]:
        staticComponents.append(component)
        continue

    if componentType in ["Earring", "Glasses", "Hat", "Necklace", "Shirt", "Face Piercing"]:
        accessories.append(component)
        continue
    
    raise "unhandled component type"

# print("static components:")
# pprint(staticComponents)
# print("accessories:")
# pprint(accessories)

# write to files

json.dump(accessories, open("./accessories.json", "w"))
json.dump(staticComponents, open("./static_components.json", "w"))