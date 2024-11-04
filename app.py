from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    if 'hello' in user_input.lower():
        return "Hello! How can I assist you today?"
    elif 'weather' in user_input.lower():
        return "I can't check the weather right now, but I hope it's nice where you are!"
    else:
        return "I'm here to help with any questions!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
