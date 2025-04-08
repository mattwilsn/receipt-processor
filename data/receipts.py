from dataclasses import dataclass

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
    id:int