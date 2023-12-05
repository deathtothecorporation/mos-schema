import json
import id_transform
from pprint import pprint

# each entry in the list should include:
#   - the id
#   - the type and variant
#   - the path to the image
#   - the number of soulbound instances
#   - the bonding curve parameter

# load list of accessories
accessories = json.load(open("./accessories.json", "r"))

# make a dictionary of id -> other data
accessoryData = {}
for accessory in accessories:
    id = id_transform.typeAndVariantToId(accessory[0], accessory[1])
    accessoryData[id] = {
        "typeId": id_transform.stringToHashToUint128(accessory[0]),
        "typeIdAsStr": str(id_transform.stringToHashToUint128(accessory[0])),
        "typeName": accessory[0],
        "variantId": id_transform.stringToHashToUint128(accessory[1]),
        "variantIdAsStr": str(id_transform.stringToHashToUint128(accessory[1])),
        "variantName": accessory[1],
        "imagePath": f"{accessory[0]}/{accessory[1]}.png",
        "soulboundSupply": 0 # we will increment this in the next loop
    }

# load components per milady
componentsPerMilady = json.load(open("./original_components_per_milady.json", "r"))

# iterate through componentsPerMilady and tally soulboundSupply for each accessory
for components in componentsPerMilady.items():
    for (componentType, componentVariant) in components[1].items():
        componentListified = [componentType, componentVariant]
        if componentListified in accessories:
            try:
                id = id_transform.typeAndVariantToId(componentType, componentVariant)
                accessoryData[id]["soulboundSupply"] += 1
            except KeyError:
                print(f"missing data for {componentType} {componentVariant}")
                continue

def supplyToBondingCurveParameter(supply):
    return int(995000000000000000 / (supply * supply))

# now add bonding curve parameter
for accessory in accessories:
    id = id_transform.typeAndVariantToId(accessory[0], accessory[1])
    # check if supply is 0
    if accessoryData[id]["soulboundSupply"] == 0:
        raise Exception(f"accessory {accessory[0]} {accessory[1]} has 0 supply")
    accessoryData[id]["bondingCurveParameter"] = supplyToBondingCurveParameter(accessoryData[id]["soulboundSupply"])


# print("accessoryData:")
# pprint(accessoryData)

# # load old accessory data and check against it
# oldAccessoryData = json.load(open("./accessory-data.json", "r"))
# for oldAccessoryData in oldAccessoryData.values():
#     id = id_transform.typeAndVariantToId(oldAccessoryData["type"], oldAccessoryData["variant"])
#     try:
#         accessoryData[id]
#     except KeyError:
#         print(f"missing data for {oldAccessoryData['type']} {oldAccessoryData['variant']}. Id: {id}")
#         continue
#     if oldAccessoryData["soulboundSupply"] != accessoryData[id]["soulboundSupply"]:
#         print(f"mismatch for {oldAccessoryData['type']} {oldAccessoryData['variant']}: {oldAccessoryData['soulboundSupply']} vs {accessoryData[id]['soulboundSupply']}")
#     if oldAccessoryData["bondingCurveParameter"] != accessoryData[id]["bondingCurveParameter"]:
#         print(f"mismatch for {oldAccessoryData['type']} {oldAccessoryData['variant']}: {oldAccessoryData['bondingCurveParameter']} vs {accessoryData[id]['bondingCurveParameter']}")

json.dump(accessoryData, open("./accessory_data.json", "w"))

# for accessory in accessoryData.values():
#     pprint(accessory)

# # print out supplies for each accessory
# for accessory in accessories:
#     id = id_transform.typeAndVariantToId(accessory[0], accessory[1])
#     print(f"{accessoryData[id]['soulboundSupply']} {accessoryData[id]['typeName']} {accessoryData[id]['variantName']}")