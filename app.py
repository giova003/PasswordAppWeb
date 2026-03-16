from flask import Flask, request, render_template_string

app = Flask(__name__)
password_map = {}

html_template = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Password App</title>
    <style>
        body {
            background: linear-gradient(135deg, #74ebd5, #ACB6E5);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: rgba(255, 255, 255, 0.95);
            padding: 50px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.25);
            width: 400px;
        }
        h1 { font-size: 3em; margin-bottom: 30px; color: #333; }
        input { padding: 15px; font-size: 1.2em; margin: 10px 0; width: 90%; border-radius: 10px; border: 1px solid #ccc; }
        button { padding: 15px 30px; font-size: 1.2em; margin: 10px 5px; border: none; border-radius: 10px; background: linear-gradient(to right, #2575fc, #6a11cb); color: white; cursor: pointer; }
        button:hover { opacity: 0.85; transform: translateY(-2px); }
        .result { margin-top: 20px; font-size: 1.5em; color: #222; word-break: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Password Codificata</h1>
        <form method="POST">
            <input type="text" name="text" placeholder="Metti quello che vuoi codificare" required>
            <br>
            <button type="submit" name="action" value="codifica">Codifica</button>
            <button type="submit" name="action" value="decodifica">Decodifica</button>
        </form>
        {% if result %}
            <div class="result">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        action = request.form.get("action")

        if action == "codifica" and text:
            encoded = "".join([chr((ord(c)+5)%256) for c in text])
            password_map[encoded] = text
            result = f"{text} = {encoded}"
        elif action == "decodifica" and text:
            decoded = password_map.get(text, "Non trovato")
            result = f"{text} = {decoded}"

    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
