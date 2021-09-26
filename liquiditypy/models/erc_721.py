from liquiditypy.models.contract import Erc721Contract
from liquiditypy.ethereum.web3_base import Web3Base


class Erc721Asset(Web3Base):
    def __init__(self, contract: Erc721Contract, web3_rpc=None):
        super().__init__(web3_rpc=web3_rpc)
        self.contract = contract

    @property
    async def asset_contract(self):
        return self.web3.eth.contract(address=self.contract.address, abi=self.contract.abi)

    async def get_wallet_balance(self, wallet_address):
        return await self.asset_contract.functions.balanceOf(wallet_address).call()

    @property
    async def asset_name(self):
        return await self.asset_contract.functions.name().call()

    @property
    async def asset_symbol(self):
        return await self.asset_contract.functions.symbol().call()

    async def owner_of(self, asset_id:int):
        return await self.asset_contract.functions.ownerOf(asset_id).call()
    
    async def retrieve(self, asset_id: int):
        return await self.asset_contract.functions.retrieve(asset_id).call()
