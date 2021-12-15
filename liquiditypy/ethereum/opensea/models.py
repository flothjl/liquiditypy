from dataclasses import dataclass
from dateutil import parser
from enum import Enum
from liquiditypy.ethereum.base.utils import get_timestamp
from liquiditypy.ethereum.base.models import Transaction


class EventType(Enum):
    '''
    The event type to filter. 
    Can be created for new auctions, 
    successful for sales, cancelled, 
    bid_entered, 
    bid_withdrawn, 
    transfer, 
    or approve
    '''
    CREATED='created'
    SUCCESSFUL='successful'
    CANCELLED='cancelled'
    BID_ENTERED='bid_entered'
    BID_WITHDRAWN='bid_withdrawn'
    TRANSFER='transfer'
    APPROVE='approve'

class AssetContract:
    def __init__(self, asset_contract: dict):
        self.address = asset_contract.get('address')
        self.name = asset_contract.get('name')
        self.symbol = asset_contract.get('symbol')
        self.dev_seller_fee_basis_pts = asset_contract.get('dev_sellet_fee_basis_points')
        self.dev_buyer_fee_basis_pts = asset_contract.get('dev_buyer_fee_basis_points')
        self.opensea_seller_fee_basis_pts = asset_contract.get('opensea_sellet_fee_basis_points')
        self.opensea_buyer_fee_basis_pts = asset_contract.get('opensea_buyer_fee_basis_points')

class OpenSeaAsset:
    def __init__(self, open_sea_asset: dict):
        self.id: int = open_sea_asset.get('id')
        self.token_id: str = open_sea_asset.get('token_id')
        self.name: str = open_sea_asset.get('name')
        self.asset_contract: AssetContract = AssetContract(
            open_sea_asset.get('asset_contract', {})
        )

class OpenSeaTransaction:
    def __init__(self, transaction: dict):
        self.block_number=transaction.get('block_number'),
        self.timestamp=get_timestamp(transaction.get('timestamp')),
        self.transaction_hash=transaction.get('transaction_hash'),
        self.from_address=transaction.get('from_account',{}).get('address'),
        self.to_address=transaction.get('winner_account',{}).get('address')

class PaymentToken:
    def __init__(self, payment_token: dict):
        self.symbol: str = payment_token.get('symbol')
        self.address: str = payment_token.get('address')
        self.name: str = payment_token.get('name')
        self.decimals: int = payment_token.get('decimals')
        self.eth_price: str = payment_token.get('eth_price')
        self.usd_price: str = payment_token.get('usd_price')

class OpenSeaAssetEvent:
    def __init__(self, open_sea_event: dict):
        self.is_approved: bool = open_sea_event.get('approved_account')
        self.asset: OpenSeaAsset = OpenSeaAsset(open_sea_event.get('asset', {}))
        self.total_price: int = int(open_sea_event.get('total_price'))
        self.payment_token: PaymentToken = PaymentToken(open_sea_event.get('payment_token', {}))
        self.transaction: OpenSeaTransaction = OpenSeaTransaction(
            open_sea_event.get('transaction', {})
        )




