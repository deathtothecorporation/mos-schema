# mOS Schema

A place to collect various common data and resources for the Milady OS project. The master branch of this repo should be considered the single source of truth for anything covered here, including the file structure and naming scheme of `components/`.

## Historical / Data Manpilation Resources

These are likely not useful for user-facing apps and runtimes, but may be useful for various data manipulation techniques.

* `original_components_per_milady.json`
  * The "completed and corrected" list of all drawable components per milady in the original MiladyMaker set.
  * Unlike the below files, this one makes no distinction between "static components" and "accessories".
* Static Components vs Accessories
  * `static_components.json` lists all components that mOS consideres **static**: background, skin tone, eye type, etc. These are forever associated with the Avatar, and can be considered the "base doll".
  * `accessories.json` lists all components that mOS considers dynamic, aka **accessories**: earrings, hats, shirts, etc. These can be equipped, unequipped, and transferred.

## App Resources

* `components/` contains all images needed to render any Avatar from the bottom up. The file/folder structure should be preserved, as `accessory_data.json` "knows" how to find the images within that structure. Note that this includes images for both "static components" like backgrounds and "accessories" like earrings.
* `static_components_per_avatar.json` lists the static components belonging to each Milady. This can be thought of as the "genetic code" of the base doll. Rendering of an Avatar (see below) should begin with this data.
* `accessory_data.json` associates every accessory ID with various data.
  * Info included for each item:
    * `typeName` and `variantName`, i.e. "hat" and "trucker gothic milady"
    * `typeId` and `variantId`
      * `typeId` in particular is useful when constructing calls to unequip an item.
    * `imagePath`: the path to the png image of the asset, relative to the root image folder (in this repo, components/)
    * `soulboundSupply`: How many items existed within the original Milady set
    * `bondingCurveParameter`: The bonding curve parameter that is or will be set in the `LiquidAccessories` contract for the item.
* [avatar-rendering-algorithm](avatar-rendering-algorithm.md) describes how to render an Avatar, given the info in this repo and the current equip state of the Avatar.
* [item-price-algorithms](item-price-algorithms.md) explains how item mint cost and burn rewards are calculated, useful for implementing off-chain calculation of purchase/return orders.