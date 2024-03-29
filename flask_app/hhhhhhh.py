from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["input"]
        if "first aid" in question.lower():
            response = get_gemini_response(question)
            return render_template("index.html", response=response)
        else:
            return render_template("index.html", response="Please ask a question related to first aid.")
    return render_template("index.html", response="")

if __name__ == "__main__":
    app.run(debug=True)
