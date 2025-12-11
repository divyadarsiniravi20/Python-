from flask import Flask,request,jsonify
app = Flask(__name__)
items=["apple","banana","mango"]
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

if __name__=="__main__":
    app.run()