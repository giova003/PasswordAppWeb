from flask import Flask, render_template, request

app = Flask(__name__)

# Questa è una codifica semplice, puoi cambiarla come vuoi
mapping = {
    'a': '@', 'b': '#', 'c': '$', 'd': '%', 'e': '^',
    'f': '&', 'g': '*', 'h': '(', 'i': ')', 'l': '-', 
    'm': '+', 'n': '=', 'o': '!', 'p': '?', 'q': '<',
    'r': '>', 's': ':', 't': ';', 'u': '~', 'v': '`', 
    'z': '_'
}

# Inverti la mappa per decodifica
inverse_mapping = {v: k for k, v in mapping.items()}

def encode(text):
    return ''.join(mapping.get(c.lower(), c) for c in text)

def decode(text):
    return ''.join(inverse_mapping.get(c, c) for c in text)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        # decide se codificare o decodificare
        if any(c in mapping for c in text.lower()):
            result = encode(text)
        else:
            result = decode(text)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
