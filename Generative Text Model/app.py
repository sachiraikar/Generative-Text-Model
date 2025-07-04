from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        output = generator(prompt, max_length=100, num_return_sequences=1)
        generated_text = output[0]["generated_text"]
    return render_template("index.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)
