from web3 import Web3

DEFAULT_RPC = 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'

class Web3Base:
    def __init__(self, web3_rpc=DEFAULT_RPC):
        self.web3 = Web3(Web3.HTTPProvider(web3_rpc))

   

