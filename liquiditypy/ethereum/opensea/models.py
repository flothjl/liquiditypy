from dataclasses import dataclass
from enum import Enum
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


@dataclass
class OpenSeaTransaction(Transaction):
    payment_token: str = None
    transaction_amount: float = None
    token_price: float = None
