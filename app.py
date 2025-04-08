from flask import Flask
app = Flask(__name__)

@app.route("/receipts/process", methods=["POST"])
def receipts_process():
    return { "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000,threaded=False)