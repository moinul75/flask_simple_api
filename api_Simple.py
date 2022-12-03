from flask import Flask,jsonify,request

app = Flask(__name__)

students = [{'id':1, 'name': 'Udoy'},{'id':2, 'name': 'Jami'}]

@app.route('/')
def home():
    return jsonify(students)

@app.route('/add',methods=['POST'])
def add():
    students.append(request.get_json())
    return "Students added successfully"

@app.route('/update',methods=['PUT'])
def update():
    for student in students:
        if student.get('id') == request.get_json().get('id'):
            student.update(request.get_json())
    print("Successfully Updated The Id: ",request.get_json())
    return "Students updated successfully"

@app.route('/delete',methods=['DELETE'])
def delete():
    for student in range(len(students)):
        if students[student].get('id') == request.get_json().get('id'):
            del students[student]
            break
    print("Student Deleted Successfully")
    return "Student deleted successfully"
if __name__ =='__main__':
    app.run(debug=True)
    