from typing import Type
from web3 import Web3

from liquiditypy.ethereum.decoders.base import BaseDecoder
from .opensea import OpenSeaDecoder
from .exceptions import DecoderNotFound

decoder_mapper = [
    {
        "addresses": ["0x7be8076f4ea4a4ad08075c2508e481d6c946d12b"],
        "decoder": OpenSeaDecoder,
    }
]


def get_decoder(contract_address: str) -> Type[BaseDecoder]:
    for decoder in decoder_mapper:
        if Web3.toInt(hexstr=contract_address) in [
            Web3.toInt(hexstr=i) for i in decoder.get("addresses", [])
        ]:
            return decoder["decoder"]
        raise DecoderNotFound
        # Web3.toInt(hexstr=txn.to_address) == Web3.toInt(hexstr=self.address)
