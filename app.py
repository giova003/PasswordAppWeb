from flask import Flask, render_template, request

app = Flask(__name__)

# funzione semplice di codifica / decodifica
def encode_name(name):
    # trasforma ogni carattere in un simbolo casuale
    symbols = ['%', '$', '&', '/', '(', ')', '#', '@', '!']
    encoded = ''.join(symbols[ord(c) % len(symbols)] for c in name)
    return encoded

def decode_password(pw):
    # decodifica semplificata solo per demo
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
    app.run(debug=True)
