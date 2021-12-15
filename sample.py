import asyncio
import web3
from web3.main import Web3
from liquiditypy.ethereum.decoders.exceptions import DecoderNotFound
from liquiditypy.models.erc_721 import Erc721Asset
from liquiditypy.models.contract import Erc721Contract
from liquiditypy.ethereum.web3_base import Web3Base
from liquiditypy.ethereum.etherscan.etherscan_base import Etherscan
from liquiditypy.ethereum.decoders.mappers import decoder_mapper, get_decoder
from liquiditypy.creds import *
contract_address = '0x3Fe1a4c1481c8351E91B64D5c398b159dE07cbc5'

w3 = Web3Base(
    web3_rpc=WEB3_RPC
).web3

etherscan = Etherscan(
    ETHERSCAN_API_KEY,
    '0xB571d31890f6BB39AD6C26aB9dd56191a5c76970'
)


test_txn_hash = '0x3c7ccd49deb3b7e38e6c5da95e76d4434905552fdf453a3b68e4a1df3fe0b974'
txn = w3.eth.get_transaction(test_txn_hash)
to = txn.to
abi = etherscan.get_abi(to)
contract = w3.eth.contract(address=to, abi=abi["result"])
try:
    decoder = get_decoder(str(to))
    print(decoder)
    decoder(contract)
except DecoderNotFound:
    print('decoder not found')
func_obj, func_params = contract.decode_function_input(txn.input)




# print(func_obj)
# print(func_params)