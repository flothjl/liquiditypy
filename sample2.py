import json
from liquiditypy.ethereum.etherscan.etherscan_base import Etherscan
from liquiditypy.ethereum.taxes.taxes_base import Taxes

contract_address = '0x3Fe1a4c1481c8351E91B64D5c398b159dE07cbc5'
my_address = '0xB571d31890f6BB39AD6C26aB9dd56191a5c76970'
api_key = 'RWJ26FW5KQ1ZPR19QEVCMHZE72B3KTYNXV'

etherscan = Taxes(
    api_key = api_key,
    address = my_address
)

print(etherscan.erc_721_taxes())

