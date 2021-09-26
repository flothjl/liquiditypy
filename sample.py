import asyncio
import web3
from liquiditypy.models.erc_721 import Erc721Asset
from liquiditypy.models.contract import Erc721Contract
contract_address = '0x3Fe1a4c1481c8351E91B64D5c398b159dE07cbc5'

test = Erc721Asset(
    Erc721Contract(contract_address)
)

async def get_owner(i):
    if i%20 == 0:
        print(f'TokenID: {i}')
    return (i, await test.owner_of(i))

async def main():
    owners = {}
    tasks = []
    for i in range(100):
        tasks.append(asyncio.create_task(get_owner(i)))
    response = await asyncio.gather(*tasks)


    print(response)

asyncio.run(main())