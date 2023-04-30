from flask import Flask, jsonify, request
from redis import Redis
from dotenv import load_dotenv
from pathlib import Path
from middlewares import middleware

import os

dotenv_path = Path('src/env/api.env')

load_dotenv(dotenv_path=dotenv_path)
load_dotenv()

app = Flask('BotAPI')

app.wsgi_app = middleware(app.wsgi_app)

REDIS_HOST_ADRRESS = os.getenv('REDIS_HOST_ADDRESS')
REDIS_HOST_PORT = os.getenv('REDIS_HOST_PORT')
REDIS_DEFAULT_DATABASE = os.getenv('REDIS_DEFAULT_DATABASE')

redis = Redis(host=REDIS_HOST_ADRRESS, port=REDIS_HOST_PORT, db=REDIS_DEFAULT_DATABASE)

default = [
    {'host': 'host',
     'key': 'key',
     'consumer': 'consumer'}
]

@app.route('/', methods=['GET', 'POST'])
def start():
    key = request.environ['api_key']
    return f'Aplicação rodando com sucesso. API Key: {key}'

@app.route('/cache', methods=['POST'])
def onPost():
    return jsonify(default)

if __name__ == '__main__':
    app.run(debug=True)