from dataclasses import dataclass
from enum import Enum
import requests
from typing import List
from web3.eth import Eth
from liquiditypy.ethereum.base.models import Transaction
from .exceptions import EtherscanResponseError

class EtherscanEnum(Enum):
    RESULT = 'result'
    MESSAGE = 'message'
    STATUS = 'status'

class EtherscanTxnEnum(Enum):
    BLOCK_NUM = 'blockNumber'
    HASH = 'hash'
    NONCE = 'nonce'
    BLOCK_HASH = 'blockHash'
    TIMESTAMP = 'timeStamp'
    TOKEN_NAME = 'tokenName'
    TOKEN_SYMBOL = 'tokenSymbol'
    TOKEN_DECIMAL = 'tokenDecimal'
    TOKEN_ID = 'tokenID'
    GAS = 'gas'
    GAS_PRICE = 'gasPrice'
    GAS_USED = 'gasUsed'
    CUM_GAS_USED = 'cumulativeGasUsed'
    CONFIRMATIONS = 'confirmations'
    FROM = 'from'
    TO = 'to'
    CONTRACT_ADDR = 'contractAddress'
    TRANSACTION_INDEX = 'transactionIndex'


class EtherscanResponse:
    def __init__(self, raw_response: requests.models.Response):
        self.raw_response: requests.models.Response = raw_response
        self.json: dict = None
        self.message: str = None
        self.result: List[EtherscanTxn] = []
        self.status: str = '1'

        self._build_etherscan_response()

    def _get_value(self, value: EtherscanEnum):
        return self.json.get(value.value)

    def _build_etherscan_response(self):
        try:
            response_json = self.raw_response.json()
        except Exception as err:
            raise EtherscanResponseError(f'Error deserializing response {err}')
        self.json = response_json
        self.message = self._get_value(EtherscanEnum.MESSAGE)
        self.status = self._get_value(EtherscanEnum.STATUS)
        self.is_success = True if self.status == '1' else False
        txn_results = self._get_value(EtherscanEnum.RESULT)
        self.result: List[EtherscanTxn] = []
        for txn in txn_results:
            self.result.append(self._build_etherscan_txn(txn))

    def _build_etherscan_txn(self, txn: dict):
        return EtherscanTxn(
            block_number=txn.get(EtherscanTxnEnum.BLOCK_NUM.value),
            timestamp=txn.get(EtherscanTxnEnum.TIMESTAMP.value),
            hash = txn.get(EtherscanTxnEnum.HASH.value),
            nonce = txn.get(EtherscanTxnEnum.NONCE.value),
            block_hash = txn.get(EtherscanTxnEnum.BLOCK_HASH.value),
            from_address = txn.get(EtherscanTxnEnum.FROM.value),
            contract_address = txn.get(EtherscanTxnEnum.CONTRACT_ADDR.value),
            to_address = txn.get(EtherscanTxnEnum.TO.value),
            token_id=txn.get(EtherscanTxnEnum.TOKEN_ID.value),
            token_name=txn.get(EtherscanTxnEnum.TOKEN_NAME.value),
            token_symbol=txn.get(EtherscanTxnEnum.TOKEN_SYMBOL.value),
            token_decimal=txn.get(EtherscanTxnEnum.TOKEN_DECIMAL.value),
            transaction_index=txn.get(EtherscanTxnEnum.TRANSACTION_INDEX.value),
            gas=txn.get(EtherscanTxnEnum.GAS.value),
            gas_price=txn.get(EtherscanTxnEnum.GAS_PRICE.value),
            gas_used=txn.get(EtherscanTxnEnum.GAS_USED.value),
            cum_gas_used=txn.get(EtherscanTxnEnum.CUM_GAS_USED.value),
            confirmations=txn.get(EtherscanTxnEnum.CONFIRMATIONS.value)
        )

    def __repr__(self):
        return f'<EtherscanResponse Object: is_success={self.is_success}>'

@dataclass
class EtherscanTxn(Transaction):
    pass