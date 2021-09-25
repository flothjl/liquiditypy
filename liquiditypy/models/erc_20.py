from web3 import Web3
from liquiditypy.models.contract import Erc20Contract
from liquiditypy.ethereum.web3_base import Web3Base

class Erc20Asset(Web3Base):
    def __init__(self, contract: Erc20Contract, web3_rpc=None):
        super().__init__(web3_rpc=web3_rpc)
        self.contract = contract

    @property
    def asset_contract(self):
        return self.web3.eth.contract(address=self.contract.address, abi=self.contract.abi)

    def get_wallet_balance(self, wallet_address):
        wallet_balance = self.asset_contract.functions.balanceOf(wallet_address).call()
        wallet_decimals = self.asset_contract.functions.decimals().call()
        return wallet_balance / 10 ** wallet_decimals

    @property
    def asset_name(self):
        return self.asset_contract.functions.name().call()

    @property
    def asset_symbol(self):
        return self.asset_contract.functions.symbol().call()
