import os
from flask import Flask

app = Flask(__name__)

# Ortam değişkeninden 'KULLANICI' bilgisini al, yoksa 'Dünya' kullan.
kullanici_adi = os.getenv('KULLANICI', 'Dünya')

@app.route('/')
def hello():
    return f"Merhaba, {kullanici_adi}!"

if __name__ == '__main__':
    # Uygulama 5000 portundan yayın yapacak
    app.run(host='0.0.0.0', port=5000)
