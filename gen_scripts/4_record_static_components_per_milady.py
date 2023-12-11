import json

componentsPerMilady = json.load(open("./original_components_per_milady.json", "r"))
staticComponents = json.load(open("./static_components.json", "r"))
staticComponentsPerMilady = {}

for idStr, components in componentsPerMilady.items():
    print(idStr)
    staticComponentsPerMilady[idStr] = {}
    for componentType, componentVariant in components.items():
        if componentType in ["Background", "Blush", "Eyebrow", "Eyes", "Eye Color", "Face Tattoo", "Hair", "Mouth", "Neck", "Race"]:
            staticComponentsPerMilady[idStr][componentType] = componentVariant

json.dump(staticComponentsPerMilady, open("./static_components_per_milady.json", "w"), indent=4)