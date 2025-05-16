YOfrom flask import Flask, request, jsonify, render_template
import requests
import time

app = Flask(__name__)

# Your actual Gemini API key
GEMINI_API_KEY = ' Youse your API '

# Gemini API endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# API request headers
HEADERS = {
    "Content-Type": "application/json"
}

# Function to get response from Gemini
def get_gemini_response(user_input):
    payload = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            return "⚠️ Error from Gemini API: " + response.text
    except Exception as e:
        return f"❌ Something went wrong: {e}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    # Add tone or style
    styled_message = f" You are a world-class virtual sales expert for a premium software development agency. Greet visitors in a friendly, professional, and confident tone. Your goal is to understand their business pain points, growth goals, or inefficiencies, and position custom software as the most effective and profitable solution. Ask smart diagnostic questions to uncover their needs, reflect back their challenges to build trust, and explain the benefits of custom software clearly—how it saves time, scales their operations, and helps achieve business goals. Provide a relatable example of how you’ve helped a similar client, including measurable results (e.g., reduced costs, increased efficiency, or growth). Then guide them to take action by booking a free consultation or requesting a quote. Handle objections empathetically and confidently, reassuring them of our expertise and commitment to results. Keep your responses short, persuasive, engaging, and human—avoid robotic tone. Focus on value over features, and always end with a clear call to action. and make you responses maxium 3 line not ore then that  : {user_message}"
    bot_reply = get_gemini_response(styled_message)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
