import os
import requests
from flask import Flask
app = Flask(__name__)

data = {os.environ.get("PASS"): os.environ.get("IDENTIFICATOR")}

@app.route('/', methods=['HEAD'])
def send():
    requests.post(os.environ.get('LINK'), data=data)
    return ""

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
    
