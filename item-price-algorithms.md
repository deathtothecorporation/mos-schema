# Item Mint Price and Burn Reward Calculations

For the ultimate source of truth on this topic, see the relevant functions of the [LiquidAccessoires contract](https://github.com/deathtothecorporation/milady-os-contracts/blob/master/src/LiquidAccessories.sol). Here I'll summarize and explain in more accessible terms.

The **mint cost** *M* and **burn reward** *B* for a given accessory type is dependent on its **bonding curve parameter** *P* and the **current supply** of liquid accessories of this type *S*.

The **mint cost** is defined in terms of the **burn reward**, so let's define the **burn reward** first:

`B = 0.005 ETH + P * S^2`

The **mint cost** is defined as 20% above the **burn reward**:

`M = B * 1.2`

combining:

`M = (0.005 ETH + P * S^2) * 1.2`

Note that the first item mint for every accessory will cost 0.006 ETH, since S = 0.

## Multiple Items

When minting or burning more than one of a given accessory, the above calculations can be run repeatedly, each time updating S with the new supply. For example, minting the first 3 items of a given accessory would cost:

```
  (0.005 ETH + P * 0^2) * 1.2
+ (0.005 ETH + P * 1^2) * 1.2
+ (0.005 ETH + P * 2^2) * 1.2
```