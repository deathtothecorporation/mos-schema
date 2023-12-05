import json

componentsPerMilady = json.load(open("./original_components_per_milady.json", "r"))

for id in componentsPerMilady.keys():
    if "Face Decoration" in componentsPerMilady[id].keys():
        if "tattoo" in componentsPerMilady[id]["Face Decoration"]:
            print(f"Tattoo:  \t{componentsPerMilady[id]['Face Decoration']}")
            componentsPerMilady[id]["Face Tattoo"] = componentsPerMilady[id]["Face Decoration"]
        else:
            print(f"Piercing:\t{componentsPerMilady[id]['Face Decoration']}")
            componentsPerMilady[id]["Face Piercing"] = componentsPerMilady[id]["Face Decoration"]
        del componentsPerMilady[id]["Face Decoration"]

json.dump(componentsPerMilady, open("./original_components_per_milady.json", "w"))