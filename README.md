# mOS Schema

A place to collect various common data and resources for the Milady OS project. The master branch of this repo should be considered the single source of truth for anything covered here, including the file structure and naming scheme of `components/`.

* `components/` contains all images needed to render any Avatar from the bottom up. The file/folder structure should be preserved, as `accessory_data.json` "knows" how to find the images within that structure. Note that this includes images for both "static components" like backgrounds and "accessories" like earrings.
* `original_components_per_milady.json`: probably unneeded in all of MiladyOS. This is the "completed and corrected" list of all drawable components per milady in the original MiladyMaker set, *making no distinction between "static components" like background and "accessories" like earrings*. MiladyOS should never use this file, but should instead look at the following files and the current equip state of a Milady Avatar to render it.
* `static_components.json` lists all possible components that are not accessories - background, skin tone, etc.
* `accessories.json` lists all accessories - aka "dynamic components" - things that can be bought and sold, and equipped/unequipped, within the Milady system. Earrings, glasses, shirts, etc. Note that if you're already using `accessory_data.json`, you probably don't need this file. Keeping it here mostly because it's the counterpart to `static_components.json`.
* `static_components_per_milady.json` lists the static components belonging to each Milady. This can be thought of as the "genetic code" of the base doll.
* `accessory-data.json` associates every accessory ID with various data.
  * Info included for each item:
    * `typeName` and `variantName`, i.e. "hat" and "trucker gothic milady"
    * `typeId` and `variantId`
      * `typeId` in particular is useful when constructing calls to unequip an item.
    * `imagePath`: the path to the png image of the asset, relative to the root image folder (in this repo, components/)
    * `soulboundSupply`: How many items existed within the original Milady set
    * `bondingCurveParameter`: The bonding curve parameter that is or will be set in the `LiquidAccessories` contract for the item.
* [avatar-rendering-algorithm](avatar-rendering-algorithm.md) describes how to render an Avatar, given the info in this repo and the current equip state of the Avatar.
* [item-price-algorithms](item-price-algorithms.md) explains how item mint cost and burn rewards are calculated, in case someone wants to calculate this off-chain.