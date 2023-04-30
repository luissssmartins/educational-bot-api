from flask import Flask, jsonify
from redis import Redis
from dotenv import load_dotenv
from pathlib import Path

import os

dotenv_path = Path('src/env/api.env')

load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

load_dotenv()

REDIS_HOST_ADRRESS = os.getenv('REDIS_HOST_ADDRESS')
REDIS_HOST_PORT = os.getenv('REDIS_HOST_PORT')
REDIS_DEFAULT_DATABASE = os.getenv('REDIS_DEFAULT_DATABASE')

redis = Redis(host=REDIS_HOST_ADRRESS, port=REDIS_HOST_PORT, db=REDIS_DEFAULT_DATABASE)

default = [
    {'host': 'host',
     'key': 'key',
     'consumer': 'consumer'}
]

@app.route('/')
def start():
    return 'Aplicação rodando com sucesso.'

@app.route('/cache', methods=['POST'])
def onPost():
    return jsonify(default)