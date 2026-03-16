from flask import Flask, render_template, request

app = Flask(__name__)

# Funzione semplice per codificare il nome in simboli
def encode_name(name):
    symbols = ['%', '$', '&', '/', '(', ')', '#', '@', '!']
    encoded = ''.join(symbols[ord(c) % len(symbols)] for c in name)
    return encoded

# Funzione di decodifica (solo dimostrativa)
def decode_password(pw):
    return "Decodifica non reale"

@app.route('/')
def home():
    return render_template('index.html', result="")

@app.route('/encode', methods=['POST'])
def encode():
    name = request.form['name']
    encoded = encode_name(name)
    return render_template('index.html', result=f"Password: {encoded}")

@app.route('/decode', methods=['POST'])
def decode():
    password = request.form['password']
    decoded = decode_password(password)
    return render_template('index.html', result=f"Nome originale: {decoded}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
