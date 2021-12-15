from typing import List
import requests
from liquiditypy.ethereum.base.utils import get_value_with_default, get_timestamp
from .models import EventType, OpenSeaAssetEvent

class OpenseaApi:
    """
    Base class to interact with etherscan api
    """
    BASE_URL = 'https://api.opensea.io/api/v1/events?'
    # account_address=0xB571d31890f6BB39AD6C26aB9dd56191a5c76970&event_type=transfer&only_opensea=false&offset=0&limit=20

    def __init__(
        self,
        api_key: str = None
    ):
        self.api_key: str = api_key

    def get_nft_events(
        self,
        account_address: str = None,
        event_type: EventType = None,
        only_opensea: bool = False,
        offset: int = 0,
        limit: int = 20,
        occurred_before: int = None,
        occurred_after: int = None,
        asset_contract_address: str = None
    ) -> List[OpenSeaAssetEvent]:

        params = {
            'only_opensea': only_opensea,
            'offset': offset,
            'limit': limit
        }

        if account_address:
            params['account_address'] = account_address
        if event_type:
            params['event_type'] = event_type.value
        if asset_contract_address:
            params['asset_contract_address'] = asset_contract_address
        if occurred_after:
            params['occurred_after'] = occurred_after
        if occurred_before:
            params['occurred_before'] = occurred_before

        # args = inspect.getfullargspec(self.get_nft_events)
        # print(args)
        # for k, v in locals().items():
        #     if k not in args.args:
        #         continue
        #     if k == 'self':
        #         continue
        #     if v:
        #         params[k] = v
        
        print(params)
        response = requests.get(
            f'{self.BASE_URL}',
            params=params
        )
        if response.status_code != 200:
            raise Exception(
                f'Error with http request to etherscan: {response.content}')
        
        try:
            data = response.json()
        except Exception as err:
            raise Exception(f'There was an error parsing json response: {err}')
        
        events = []
        
        if not (asset_events := data.get('asset_events')):
            return events

        for event in asset_events:
            events.append(OpenSeaAssetEvent(event))
        
        return events