from flask import Flask, render_template, request
import os

app = Flask(__name__)

mapping = {
'a':'@','b':'#','c':'$','d':'%','e':'^','f':'&','g':'*',
'h':'(','i':')','l':'-','m':'+','n':'=','o':'!','p':'?',
'q':'<','r':'>','s':':','t':';','u':'~','v':'`','z':'_'
}

inverse_mapping = {v:k for k,v in mapping.items()}

def encode(text):
    return ''.join(mapping.get(c.lower(), c) for c in text)

def decode(text):
    return ''.join(inverse_mapping.get(c, c) for c in text)

@app.route("/", methods=["GET","POST"])
def index():
    result = ""

    if request.method == "POST":
        text = request.form["text"]

        if any(c in mapping for c in text.lower()):
            result = encode(text)
        else:
            result = decode(text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
