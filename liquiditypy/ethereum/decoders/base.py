from web3.datastructures import AttributeDict
from web3 import Web3
from web3.contract import Contract


class BaseDecoder:
    """
    Base class for decoding transaction inputs
    """

    def __init__(
        self,
        contract: Contract,
    ):
        self.contract: Contract = contract
