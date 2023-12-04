# mOS Schema

A place to collect various common data and documentation for the Milady OS project. The master branch of this repo should be considered the single source of truth for anything covered here, including the file structure and naming scheme of `components/`.

Here's what I plan to collect here:

**Done:**

* `components/` contains all images needed to render any Avatar from the bottom up. The file structure is important.
* `original_components_per_milady.json`: probably unneeded in all of MiladyOS. This is the "completed and corrected" list of all drawable components per milady in the original MiladyMaker set. MiladyOS should never use this file, but should instead look at the following files and the current equip state of a Milady Avatar to render it.
* `static_components.json` lists all components that are not accessories - background, skin tone, etc.
* `accessories.json` lists all accessories - aka "dynamic components - things that can be bought and sold, and equipped/unequipped, within the Milady system.
  * This can be thought of as a subset of the next item, and is structured differently. Keeping it here mostly because it's the symmetric partner to `static_components.json`.
* `accessory-data.json`, which associates every accessory ID with various data.
  * Note that json doesn't really store ints as dictionary keys, so you may have to do a `dict[str(accId)]` rather than a straight `dict[accId]`.
  * Info included for each item:
    * `typeName` and `variantName`, i.e. "hat" and "trucker gothic milady"
    * `typeId` and `variantId`
      * `typeId` in particular is useful when constructing calls to unequip an item.
    * `imagePath`: the path to the png image of the asset, relative to the root image folder (in this repo, components/)
    * `soulboundSupply`: How many items existed within the original Milady set
    * `bondingCurveParameter`: The bonding curve parameter that should be / is set in the `LiquidAccessories` contract for the item.
* **TODO**: `static_components_per_milady.json`, a dictionary that defines the components that should always be drawn for a given milady - background, skin tone, etc. This can be thought of as the "genetic code" of the base doll.

**Todo:**

* Reference rendering script written in Python
* A reference for offline calculation of item mint cost and burn reward.