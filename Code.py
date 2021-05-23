from flask import Flask
from flask.json import jsonify, request

tasks = [{
    "id": 1,
    'Name': "Jeff",
    'Contact': 8821091231,
    'done': False
}, {
    "id": 2,
    'Name': "Ayan", 
    'Contact': 9238102318,
    'done': False
}]

app = Flask(__name__)

@app.route("/add-data", methods=["POST"])

def add_task():
    try: 
        if not request.json:
            return jsonify({
                "status": "error",
                "message": "Please provide the data!",
                "request": request.json
            }, 400)

        else: 
            contact = {
                "id": tasks[-1]['id'] + 1,
                'Name': request.json['Name'],
                'Contact': request.json.get('Contact', ""),
                'done': False
            }

            tasks.append(contact)
            print(tasks)

        return jsonify({
                "Status": "Success",
                "Message": "Task added successfully"
            })    

    except Exception as e:
        print(e)

app.run()