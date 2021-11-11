from web3.eth import Eth
from liquiditypy.ethereum.etherscan.etherscan_base import Etherscan
from liquiditypy.ethereum.etherscan.models import EtherscanEnum
class Taxes(Etherscan):
    def erc_721_taxes(self):
        tokens = []
        txns = self.erc_721_txns()
        if not txns.is_success:
            raise Exception()
        txns = txns.result
        for txn in txns:
            print(txn.get(EtherscanEnum.CONTRACT_ADDR.value))
            if (contract_address := txn.get(EtherscanEnum.CONTRACT_ADDR.value)) in tokens:
                continue
            tokens.append(contract_address)
        print(tokens)

