import json
import requests
from web3.eth import Eth
from .models import EtherscanResponse

class Etherscan:
    """
    Base class to interact with etherscan api
    """
    BASE_URL = 'https://api.etherscan.io/api'

    def __init__(
        self,
        api_key: str,
        address: str
    ):
        self.api_key: str = api_key
        self.address: str = address

    def erc_721_txns(
        self,
        start_block: int = 0,
        end_block: int = 999999999,
        sort: str = 'asc'
    ) -> EtherscanResponse:
        return self._base_token_txn_request(
            'tokennfttx',
            start_block,
            end_block,
            sort
        )

    def erc_20_txns(
        self,
        start_block: int = 0,
        end_block: int = 999999999,
        sort: str = 'asc'
    ):
        return self._base_token_txn_request(
            'tokentx',
            start_block,
            end_block,
            sort
        )

    def _base_token_txn_request(
        self,
        action: str,
        start_block: int = 0,
        end_block: int = 999999999,
        sort: str = 'asc'
    ) -> EtherscanResponse:
        response = requests.get(
            f'{self.BASE_URL}',
            params={
                'module': 'account',
                'action': action,
                'address': self.address,
                'startblock': start_block,
                'endblock': end_block,
                'sort': sort,
                'apikey': self.api_key
            }
        )
        if response.status_code != 200:
            raise Exception(
                f'Error with http request to etherscan: {response.content}')
        return EtherscanResponse(response)
