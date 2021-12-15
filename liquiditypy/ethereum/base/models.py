from dataclasses import dataclass

@dataclass
class Transaction:
    block_number: str = None
    timestamp: int = None
    transaction_hash: str = None
    nonce: str = None
    block_hash: str = None
    from_address: str = None
    contract_address: str = None
    to_address: str = None
    token_id: str = None
    token_name: str = None
    token_symbol: str = None
    token_decimal: str = None
    transaction_index: str = None
    gas: str = None
    gas_price: str = None
    gas_used: str = None
    cum_gas_used: str = None
    confirmations: str = None