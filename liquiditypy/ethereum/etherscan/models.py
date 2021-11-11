from enum import Enum
import requests


class EtherscanEnum(Enum):
    RESULT = 'result'
    MESSAGE = 'message'
    STATUS = 'status'
    BLOCK_NUM = 'blockNumber'
    HASH = 'hash'
    NONCE = 'nonce'
    BLOCK_HASH = 'blockHash'
    TOKEN_NAME = 'tokenName'
    TOKEN_SYMBOL = 'tokenSymbol'
    TOKEN_DECIMAL = 'tokenDecimal'
    GAS = 'gas'
    GAS_PRICE = 'gasPrice'
    GAS_USED = 'gasUsed'
    CUM_GAS_USED = 'cumulativeGasUsed'
    CONFIRMATIONS = 'confirmations'
    FROM = 'from'
    TO = 'to'
    CONTRACT_ADDR = 'contractAddress'


class EtherscanResponse:
    def __init__(self, raw_response: requests.models.Response):
        self.raw_response: requests.models.Response = raw_response
        self.json: dict = None
        self._build_etherscan_response()

    @property
    def result(self):
        return self.json.get(EtherscanEnum.RESULT.value)

    @property
    def message(self):
        return self.json.get(EtherscanEnum.MESSAGE.value)

    @property
    def status(self):
        return self.json.get(EtherscanEnum.STATUS.value, '-1')

    @property
    def is_success(self):
        if self.status == '1':
            return True
        return False

    def _build_etherscan_response(self):
        try:
            response_json = self.raw_response.json()
        except Exception as err:
            raise Exception(f'Error deserializing response {err}')
        self.json = response_json
    
    def __repr__(self):
        return f'<EtherscanResponse Object: is_success={self.is_success}>'
