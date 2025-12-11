from flask import Flask,request,jsonify
app = Flask(__name__)
employees=["Divya" , "Anu", "Kanishq","Kavya"]

@app.route("/details",methods=["GET"])
def get_details():
    return jsonify(employees)

@app.route("/details",methods=["POST"])
def add_employee():
    data = request.get_json()
    new_employee = data.get("employees")
    employees.append(new_employee)
    return "POST EXECUTED"

@app.route("/details/<int:i>",methods=["PUT"])
def update_employee(i):
    data = request.get_json()
    new_employee = data.get("employees")
    employees[i] = new_employee
    return "PUT EXECUTED"

@app.route("/details/<int:i>",methods=["DELETE"])
def delete_employee(i):
    employees.pop(i)
    return "DELETE EXECUTED"

if __name__=="__main__":
    app.run(debug=True)