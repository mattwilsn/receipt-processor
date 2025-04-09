from data.receipts import Receipt, list_of_receipts
from services.calculatePoints import PointsCalculator
import uuid
import json
import dataclasses


class ReceiptsProcessPontroller:

    def process_receipt(receipt):
        id =  str(uuid.uuid4())
        """
        Store a single receipt and return id. of the new receipt
        """
        receipt = Receipt(
            receipt.get("retailer"), 
            receipt.get("purchaseDate"), 
            receipt.get("items"),
            float(receipt.get("total")),
            receipt.get("purchaseTime")
        )
        
        list_of_receipts[id]= receipt
        
        return id
  
    
    def get_points(id):
        """
        Get points for a single receipt
        """
        if id in list_of_receipts:
            pc = PointsCalculator()
            total = pc.calculate_points(list_of_receipts[id])
            return {"points": total}
        else:
            return {"error": "Receipt not found"}
        return None

