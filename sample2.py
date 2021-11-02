import asyncio
from liquiditypy.ethereum.web3_base import Web3Base
from liquiditypy.models.contract import Erc721Contract
contract_address = '0x3Fe1a4c1481c8351E91B64D5c398b159dE07cbc5'

test = Web3Base(is_async=True).web3.eth

async def get_current_block():
    return test.get_block(block_identifier=test.default_block, full_transactions=False)

async def main():
    print(await get_current_block())

asyncio.run(main())