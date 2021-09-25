import web3
from liquiditypy.models.erc_721 import Erc721Asset
from liquiditypy.models.contract import Erc721Contract
contract_address = '0x3Fe1a4c1481c8351E91B64D5c398b159dE07cbc5'

test = Erc721Asset(
    Erc721Contract(contract_address)
)


print(test.owner_of(929))