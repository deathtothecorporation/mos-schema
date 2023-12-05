import id_transform
import json

accessoryData = json.load(open("./accessory_data.json", "r"))
accessories = json.load(open("./accessories.json", "r"))

for accessory in accessories:
    # check we have the data
    found = False
    for accIdStr, accData in accessoryData.items():
        if [accData["typeName"], accData["variantName"]] == accessory:
            found = True
            break
    
    if not found:
        print(f"missing data for {accessory}")