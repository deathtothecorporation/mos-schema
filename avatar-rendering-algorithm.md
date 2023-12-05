For an implementation of this algorithm, see the `renderAvatar` function in [render-avatar-scripts/src/render_avatars.py](https://github.com/deathtothecorporation/avatar-render-scripts/blob/master/src/render_avatars.py), but the underlying algorithm is so simple you probably don't even need to reference it.

# Rendering an Avatar

Here's how you render an avatar with a given `id`:

1. Get the dictionary of static components for the avatar from `static_components_per_milady.json`.
2. Replace the "Eyes" and "Eye Color" entries with a single combined "Eyes" entry, where its value is formed by joining the eye type string to the color string with an underscore. For example, the `"Eyes": "teary"` and `"Eye Color": "blue"` entries should be removed, and replaced with an `"Eyes", "teary_blue"` entry.
3. Get an updated list of equipped accessories from the avatar. [render-avatar-scripts/src/update_equip_status.py](https://github.com/deathtothecorporation/avatar-render-scripts/blob/master/src/update_equip_status.py) does this and saves the result in `data/equip_state.json`.
   * `equip_state.json` expresses the list of accessories by their `accessoryId`. Convert these to `accessoryType: accessoryVariant` associations by looking up these values in the `accessory_data.json` object.
4. Combine the above two sources of data (static components and accessories) into a single dictionary that maps `componentType`s to `componentVariant`s.

By this point you should have something that looks like this, which we can call `drawableComponents`:

```
{'Background': 'bjork',
 'Eyebrow': 'complacentb',
 'Eyes': 'classic_green',
 'Face Piercing': 'nose ring silver',
 'Hair': 'tuft green',
 'Hat': 'white cowboy hat',
 'Mouth': 'crooked',
 'Race': 'pale',
 'Shirt': 'pink knit polo'}
```

5. Draw each component, in this order: `["Background", "Race", "Neck", "Necklace", "Shirt", "Blush", "Mouth", "Eyes", "Face Tattoo", "Face Piercing", "Hair", "Earring", "Eyebrow", "Glasses", "Hat"]`
   * Not all of components always appear, so skip types that `drawableComponents` doesn't have.
   * The image assets are organized in folders by type, and labelled by their variant. So for example, the eyes asset above would have the local path `Eyes/classic_green.png`; in this repo that would mean the asset would be found at `./components/Eyes/classic_green.png`.
   * Each asset should be layered on top of the previous one via alpha composition.