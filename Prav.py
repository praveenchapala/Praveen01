from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API Key
openai.api_key = "your_openai_api_key"

def generate_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=100
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return "Sorry, I couldn't process your request right now."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

