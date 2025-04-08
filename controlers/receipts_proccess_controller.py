from data.receipts import Receipt
import uuid

class receipts_process_controller:
    def __init__(self):
        pass

    def process_receipt(receipt):
        id =  uuid.uuid4()
        """
        Process a single receipt and return id. of the new receipt
        """
        card1 = Receipt(
            receipt.get("retailer"), 
            receipt.get("purchaseDate"), 
            receipt.get("total"), 
            receipt.get("items"),
           id
            )
        return id