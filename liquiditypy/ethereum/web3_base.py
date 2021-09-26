from web3 import Web3

DEFAULT_RPC = 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'

class Web3Base:
    def __init__(self, web3_rpc=DEFAULT_RPC):
        self._web3_rpc = web3_rpc
        if not self._web3_rpc:
            self._web3_rpc = DEFAULT_RPC
        self.web3 = Web3(Web3.AsyncHTTPProvider(self._web3_rpc))


   

