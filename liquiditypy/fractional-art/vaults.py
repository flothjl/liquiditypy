import json
from web3 import Web3

SINGLE_NFT_VAULT = '0x85aa7f78bdb2de8f3e0c0010d99ad5853ffcfc63'
BASKET_NFT_VAULT = '0xde771104C0C44123d22D39bB716339cD0c3333a1'

ethereum = Web3(Web3.HTTPProvider(
    'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'))

