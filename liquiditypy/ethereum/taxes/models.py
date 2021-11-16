import datetime
from typing import List, Union

from liquiditypy.ethereum.etherscan.models import EtherscanTxn

class TaxEvent:
    def __init__(
        self,
        etherscan_txn: EtherscanTxn
    ):
        self.contract: str = etherscan_txn.contract_address
        self.buy_date: datetime.datetime = None
        self.sell_date: datetime.datetime = None
        self.buy_price: float = None
        self.sell_price: float = None
        self.raw_transactions: List[dict] = []
        self.token_id = etherscan_txn.token_id
        self.from_address = etherscan_txn.from_address
        self.to_address = etherscan_txn.to_address

    def _build_tax_txn(self):
        return

    def __contains__(self, contract, token):
        if contract == self.contract and token == self.token_id:
            return True
        return False
