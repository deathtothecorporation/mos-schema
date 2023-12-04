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
    if componentType in ["Background", "Blush", "Eyebrow", "Eyes", "Hair", "Mouth", "Neck", "Race"]:
        staticComponents.append(component)
        continue

    if componentType in ["Earrings", "Glasses", "Hat", "Necklace", "Shirt"]:
        accessories.append(component)
        continue

    if componentType == "Face Decoration":
        if componentVariant in ["face piercings", "nose ring gold", "nose ring silver", "snakebites"]:
            accessories.append(component)
            continue
        
        else:
            staticComponents.append(component)
            continue
    
    raise "unhandled component type"

# write to files

print("static components:")
pprint(staticComponents)
print("accessories:")
pprint(accessories)

json.dump(accessories, open("./accessories.json", "w"))
json.dump(staticComponents, open("./static_components.json", "w"))