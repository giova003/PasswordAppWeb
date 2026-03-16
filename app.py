from flask import Flask, render_template_string, request

app = Flask(__name__)

# Dizionario temporaneo per Crea codice/Scopri codice
password_map = {}

HTML_TEMPLATE = """
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
            transition: transform 0.3s ease;
        }
        .container:hover { transform: scale(1.02); }
        h1 { font-size: 3em; margin-bottom: 30px; color: #333; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
        input { padding: 15px; font-size: 1.2em; margin: 10px 0; width: 90%; border-radius: 10px; border: 1px solid #ccc; transition: border 0.3s ease, box-shadow 0.3s ease; }
        input:focus { border-color: #2575fc; box-shadow: 0 0 10px rgba(37,117,252,0.5); outline: none; }
        select { padding: 10px; font-size: 1.1em; margin: 10px 0; border-radius: 10px; border: 1px solid #ccc; }
        button { padding: 15px 30px; font-size: 1.2em; margin: 10px 0; border: none; border-radius: 10px; background: linear-gradient(to right, #2575fc, #6a11cb); color: white; cursor: pointer; transition: 0.3s; }
        button:hover { opacity: 0.85; transform: translateY(-2px); }
        .result { margin-top: 20px; font-size: 1.5em; color: #222; word-break: break-word; display: flex; justify-content: center; align-items: center; gap: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Password Codificata</h1>
        <form method="POST">
            <input type="text" name="text_input" placeholder="Metti quello che vuoi codificare" required>
            <br>
            <select name="action">
                <option value="Crea codice">Crea codice</option>
                <option value="Scopri codice">Scopri codice</option>
            </select>
            <br>
            <button type="submit">Genera</button>
        </form>

        {% if result %}
            <div class="result">
                {{ result }}
                <button type="button" onclick="copyResult()">Copia</button>
            </div>
        {% endif %}
    </div>

    <script>
        function copyResult() {
            const resultText = document.querySelector('.result').innerText.replace('Copia','').trim();
            navigator.clipboard.writeText(resultText).then(() => { alert('Testo copiato!'); });
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form.get("text_input", "").strip()
        action = request.form.get("action")

        if action == "Crea codice" and text:
            encoded = "".join([chr((ord(c)+5)%256) for c in text])
            password_map[encoded] = text
            result = encoded
        elif action == "Scopri codice" and text:
            decoded = password_map.get(text, "Non trovato")
            result = decoded

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 
