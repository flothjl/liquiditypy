from liquiditypy.models.default_abis import ERC_20_ABI_BASE, ERC_721_ABI_BASE
class Contract:
    def __init__(self, address: str, abi: list):
        self.address = address
        self.abi = abi

class Erc20Contract(Contract):
    def __init__(self, address: str, abi: list= ERC_20_ABI_BASE):
        super().__init__(address, abi=abi)


class Erc721Contract(Contract):
    def __init__(self, address: str, abi: list= ERC_721_ABI_BASE):
        super().__init__(address, abi=abi)