from data.receipts import Receipt, list_of_receipts
from services.calculatePoints import PointsCalculator
import uuid
import json
import dataclasses


class receipts_process_controller:
   
    def get_receipts():
        """
        Get all receipts
         """
        return list_of_receipt

    def __init__(self):
        pass

    def process_receipt(receipt):
        id =  str(uuid.uuid4())
        """
        Process a single receipt and return id. of the new receipt
        """
        receipt = Receipt(
            receipt.get("retailer"), 
            receipt.get("purchaseDate"), 
            receipt.get("total"), 
            receipt.get("items")
        )
        
        list_of_receipts[id]= receipt

        return list_of_receipts
  
    
    def get_points(id):
    

        """
        Get points for a single receipt
        """
        if id in list_of_receipts:
            pc = PointsCalculator()
            total = pc.calculate_points(list_of_receipts[id])
            # receipt_data_class = list_of_receipts[id]
            # receipt_dict = dataclasses.asdict(receipt_data_class)
            # receipt_json = json.dumps(receipt_dict)
            return total
        return None

