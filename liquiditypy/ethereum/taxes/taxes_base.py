from datetime import datetime
from liquiditypy.ethereum.etherscan.etherscan_base import Etherscan
from liquiditypy.ethereum.etherscan.models import EtherscanTxnEnum
from typing import List
from web3 import Web3
from liquiditypy.ethereum.taxes.models import TaxEvent


class Taxes(Etherscan):
    def erc_721_tax_txns(self) -> List[TaxEvent]:
        events = []
        txns = self.erc_721_txns()

        if not txns.is_success:
            raise Exception()

        for txn in txns.result:
            if Web3.toInt(hexstr=txn.to_address) == Web3.toInt(hexstr=self.address):
                events.append(TaxEvent(txn))
        return events
