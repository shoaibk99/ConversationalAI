from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def index():
    return jsonify({
        "student_number": "YourStudentNumber"  # Replace with your actual student number
    })

# Route for Dialogflow webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    if intent_name == 'Admission Deadlines Intent':
        response_text = "The admission deadline for both Math and Machine Learning courses is August 31st."
    else:
        response_text = "I'm not sure how to help with that."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
