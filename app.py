from flask import Flask, render_template, request

app = Flask(__name__)

# Dizionario per memorizzare codifica/decodifica temporanea
password_map = {}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form.get("text_input", "").strip()
        action = request.form.get("action")
        
        if action == "codifica" and text:
            # Genera una codifica semplice basata su simboli
            encoded = "".join([chr((ord(c)+5)%256) for c in text])
            password_map[encoded] = text
            result = f"{text} = {encoded}"
        elif action == "decodifica" and text:
            decoded = password_map.get(text, "Non trovato")
            result = f"{text} = {decoded}"
            
    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
