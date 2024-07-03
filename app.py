from flask import Flask, render_template, request, jsonify
import requests

## Webhook URL von RASA
RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'

app = Flask(__name__)

## Verknüpfung zur HTML
@app.route('/')
def index():
    return render_template('index.html')

## Verarbeitung User Input und Response senden
@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # sende eingabe an RASA
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I did not understand that. Maybe you should restart the chat'

    return jsonify({'response': bot_response})


if __name__ == "__main__":
    app.run(debug=True)
