from flask import Flask, jsonify
import os

#create app
app = Flask(__name__)

#set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
