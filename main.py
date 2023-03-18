import os
import requests
from flask import Flask
app = Flask(__name__)

data = {os.environ.get("PASS"): os.environ.get("IDENTIFICATOR")}

@app.before_request
def send():
    try:
        requests.post(os.environ.get('LINK'), data=data, timeout=10)
    except requests.exceptions.ReadTimeout:
        pass
    return ""

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
    
