from data.receipts import Receipt, list_of_receipts
import uuid

class receipts_process_controller:
    def __init__(self):
        pass

    def process_receipt(receipt):
        id =  uuid.uuid4()
        """
        Process a single receipt and return id. of the new receipt
        """
        receipt = Receipt(
            receipt.get("retailer"), 
            receipt.get("purchaseDate"), 
            receipt.get("total"), 
            receipt.get("items"),
           id
            )
        list_of_receipts.append(receipt)
        return id
    
    def get_points(id):

        """
        Get points for a single receipt
        """
        for receipt in list_of_receipts:
            if str(receipt.id) == id:
                return str(receipt.id)
        pass