from dataclasses import dataclass
import uuid

@dataclass
class Item:
    shortDescription: str
    price: float


@dataclass
class Receipt:
    retailer: str
    purchaseDate: str
    items: list[Item]
    total: float
    purchaseTime: str

list_of_receipts = {}