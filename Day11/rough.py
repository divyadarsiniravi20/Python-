from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
list=["anu","Arthi"]
@app.route("/peoples",methods=["GET"])
def peoples():
    return jsonify(list)
