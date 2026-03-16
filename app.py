from flask import Flask, request, render_template_string

app = Flask(__name__)

import string, random
random.seed(42)
chars = string.ascii_letters + string.digits + string.punctuation + " "
shuffled = list(chars)
random.shuffle(shuffled)
mappa = dict(zip(chars, shuffled))
mappa_inv = dict(zip(shuffled, chars))

HTML = """
<!doctype html>
<title>Password Encoder</title>
<h2>Password Encoder</h2>
<form method="POST">
  <input name="text" placeholder="Inserisci nome o codice" size="40" required>
  <button name="action" value="encode">Codifica</button>
  <button name="action" value="decode">Decodifica</button>
</form>
<p>Risultato: {{result}}</p>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        action = request.form["action"]
        if action == "encode":
            result = ''.join(mappa.get(c, c) for c in text)
        else:
            result = ''.join(mappa_inv.get(c, c) for c in text)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
