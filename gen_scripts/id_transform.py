from web3 import Web3
w3 = Web3()

# transform type and variant to id
def stringToHashToUint128(s):
    hashed = w3.keccak(text=s).hex()
    hashedAsInt = int(hashed, 16)
    # trim to 128 bits
    return hashedAsInt & (2**128 - 1)

def typeAndVariantToId(type, variant):
    return stringToHashToUint128(type) << 128 | stringToHashToUint128(variant)