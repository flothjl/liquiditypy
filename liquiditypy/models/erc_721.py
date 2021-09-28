from liquiditypy.models.contract import Erc721Contract
from liquiditypy.ethereum.web3_base import Web3Base


class Erc721Asset(Web3Base):
    def __init__(self, contract: Erc721Contract, web3_rpc=None, is_async=True):
        super().__init__(web3_rpc=web3_rpc, is_async=is_async)
        self.contract = contract

    @property
    def asset_contract(self):
        return self.web3.eth.contract(address=self.contract.address, abi=self.contract.abi)

    def get_wallet_balance(self, wallet_address):
        return self.asset_contract.functions.balanceOf(wallet_address).call()

    @property
    def asset_name(self):
        return self.asset_contract.functions.name().call()

    @property
    def asset_symbol(self):
        return self.asset_contract.functions.symbol().call()

    def owner_of(self, asset_id:int):
        return self.asset_contract.functions.ownerOf(asset_id).call()
    
    def retrieve(self, asset_id: int):
        return self.asset_contract.functions.retrieve(asset_id).call()
