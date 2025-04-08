from dataclasses import dataclass
import uuid

@dataclass
class Item:
    shortDescription: str
    price: str


@dataclass
class Receipt:
    retailer: str
    purchaseDate: str
    total: str
    items: list[Item]
    id:uuid

list_of_receipts = []