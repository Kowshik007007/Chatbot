from flask import Flask, render_template, request, jsonify  # Fix typo in 'request'

from chat import get_response  # Assuming you have a function 'get_response' in chat.py

app = Flask(__name__)  # Initialize Flask app here

@app.get("/")
def index_get():  # Fixed function declaration syntax
    return render_template("base.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get("message")  # Fixed typo in 'request'
    # TODO: check if text is valid

    response = get_response(text)
    message = {"answer": response}  # Fixed assignment syntax
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)  # This should run the app when executed
