from flask import Flask, request
from controlers.receipts_proccess_controller import receipts_process_controller

app = Flask(__name__)

@app.route("/receipts/process", methods=["POST"])
def receipts_process():
    data = request.get_json()
    if not data:
        return { "error": "No data provided" }, 400    
    id = receipts_process_controller.process_receipt(data)

    return {"id": id}, 200


@app.route("/receipts/<id>/points", methods=["GET"])
def get_points(id):
    if not id:
        return { "error": "No id provided" }, 400    
    
    points = receipts_process_controller.get_points(id)

    return {"points": points}, 200

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000,threaded=False)