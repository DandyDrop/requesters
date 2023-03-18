import os
import requests
from flask import Flask
app = Flask(__name__)

@app.before_request
def send():
    try:
        requests.post(os.environ.get('LINK'), timeout=3)
    except requests.exceptions.ReadTimeout:
        pass
    return ""

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
    
