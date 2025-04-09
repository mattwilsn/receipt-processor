from flask import Flask, request
from controlers.receiptsProccessController import ReceiptsProcessPontroller

app = Flask(__name__)

@app.route("/receipts/process", methods=["POST"])
def receipts_process():
    data = request.get_json()
    if not data:
        return { "error": "No data provided" }, 400    
    id = ReceiptsProcessPontroller.process_receipt(data)

    return {"id": id}, 200


@app.route("/receipts/<id>/points", methods=["GET"])
def get_points(id):
    if not id:
        return { "error": "No id provided" }, 400    
    
    results = ReceiptsProcessPontroller.get_points(id)
    
    if "error" in results:
        return { "error": results["error"]}, 404

    return results, 200

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000,threaded=False)