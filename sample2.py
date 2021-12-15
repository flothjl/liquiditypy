import json
from liquiditypy.ethereum.etherscan.etherscan_base import Etherscan
from liquiditypy.ethereum.taxes.taxes_base import Taxes

from liquiditypy.ethereum.opensea.opensea_api_base import Opensea
from liquiditypy.ethereum.opensea.models import EventType
from liquiditypy.creds import ETHERSCAN_API_KEY

contract_address = '0x3Fe1a4c1481c8351E91B64D5c398b159dE07cbc5'
my_address = '0xB571d31890f6BB39AD6C26aB9dd56191a5c76970'
api_key = ETHERSCAN_API_KEY

os = Opensea()

values = os.get_nft_events(
    account_address=my_address,
    event_type=EventType.SUCCESSFUL
)
