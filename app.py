from flask import Flask, request
from controlers.receipts_proccess_controller import receipts_process_controller

app = Flask(__name__)

@app.route("/receipts/process", methods=["POST"])
def receipts_process():
    data = request.get_json()
    if not data:
        return { "error": "No data provided" }, 400
    
    id = receipts_process_controller.process_receipt(data)
    
    print("Data received:", data)


    return {"retailer": data.get("retailer"), "total": id}, 200

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000,threaded=False)