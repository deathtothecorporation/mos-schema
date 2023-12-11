# mOS Schema

A place to collect various common data and resources for the Milady OS project. The master branch of this repo should be considered the single source of truth for anything covered here, including the file structure and naming scheme of `components/`.

* `components/` contains all images needed to render any Avatar from the bottom up. The file/folder structure should be preserved, as `accessory_data.json` "knows" how to find the images within that structure. Note that this includes images for both "static components" like backgrounds and "accessories" like earrings.
* `original_components_per_milady.json`
  * probably unneeded in all of MiladyOS, because unlike the below files, this one makes no distinction between "static components" like background and "accessories" like earrings, and treats all components as permanently associated with a given Milady, which is not true in mOS for accessories.
  * This is the "completed and corrected" list of all drawable components per milady in the original MiladyMaker set.
* Static Components vs Accessories
  * All components are either static components (like background, skin tone, eye type) and can be considered part of the base doll; or accessories, which can be equipped/unequipped and transferred.
  * These files may be helpful in various data manipulation tasks, but are likely not useful for user-facing runtimes. For those, see `static_components_per_milady.json` and `accessory_data.json`.
  * `static_components.json` lists all static components in mOS.
  * `accessories.json` lists all accessories in mOS.
* `static_components_per_milady.json` lists the static components belonging to each Milady. This can be thought of as the "genetic code" of the base doll. Rendering of an Avatar (see below) should begin with this data.
* `accessory-data.json` associates every accessory ID with various data.
  * Info included for each item:
    * `typeName` and `variantName`, i.e. "hat" and "trucker gothic milady"
    * `typeId` and `variantId`
      * `typeId` in particular is useful when constructing calls to unequip an item.
    * `imagePath`: the path to the png image of the asset, relative to the root image folder (in this repo, components/)
    * `soulboundSupply`: How many items existed within the original Milady set
    * `bondingCurveParameter`: The bonding curve parameter that is or will be set in the `LiquidAccessories` contract for the item.
* [avatar-rendering-algorithm](avatar-rendering-algorithm.md) describes how to render an Avatar, given the info in this repo and the current equip state of the Avatar.
* [item-price-algorithms](item-price-algorithms.md) explains how item mint cost and burn rewards are calculated, useful for implementing off-chain calculation of purchase/return orders.