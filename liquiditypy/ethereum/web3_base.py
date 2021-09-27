from web3 import Web3
from web3.providers import rpc


DEFAULT_HTTP_RPC = 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
DEFAULT_WS_RPC = 'wss://mainnet.infura.io/ws/v3/24ea51066f304e5d971ee63991ae4276'


class Web3Base:
    def __init__(self, web3_rpc=None):
        self._web3_rpc = web3_rpc

        if not self._web3_rpc:
            self._web3_rpc = DEFAULT_WS_RPC

        self.web3 = self._build_web3(self._web3_rpc)
        print(self._web3_rpc)

    def _build_web3(self, rpc_provider: str, is_async: bool = False) -> Web3:
        provider_type = rpc_provider.split('://')
        if len(provider_type) < 2:
            raise
        provider_type = provider_type[0].lower()
        if provider_type in ['ws', 'wss']:
            return Web3(Web3.WebsocketProvider(rpc_provider))
        if provider_type in ['http', 'https']:
            if is_async:
                return Web3(Web3.AsyncHTTPProvider(rpc_provider))
            return Web3(Web3.HTTPProvider(rpc_provider))
