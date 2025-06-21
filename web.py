from flask import Flask, jsonify, render_template_string, request
import random
import json
import subprocess
import platform
import time
import requests
import threading
import os

app = Flask(__name__)
request_log = {}
ngl_log = {}
ACTIVE_USERS = {}
STOP_FLAGS = {}
user_locks = {}
VALID_KEY = "zprojectduongcongbang"

def load_videos():
    with open('vdtet.json', 'r') as file:
        data = json.load(file)
    return data['videos']

@app.route('/')
def home():
    return render_template_string('''
        <html>
        <head>
            <style>
                body { background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=80'); background-size: cover; background-position: center; color: white; text-align: center; padding-top: 20%; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                a { color: #00FFEF; text-decoration: none; font-size: 22px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Khiem's API</h1>
            <ul>
                <li><a href="/gai?key=[key]">API VIDEO GÁI</a></li>
                <li><a href="/sms?sdt=your_number&key=[key]">Send SMS API</a></li>
                <li><a href="/ngl?username=your_username&message=your_message&key=[key]">Send NGL Message API</a></li>
            </ul>
        </body>
        </html>
    ''')

@app.route('/gai', methods=['GET'])
def random_video():
    videos = load_videos()
    video = random.choice(videos)
    key = request.args.get('key')
    if key != VALID_KEY:
        return jsonify({'error': 'Invalid key. Access denied.'}), 403
    return jsonify({'video': video})

@app.route('/ngl', methods=['GET'])
def send_ngl():
    username = request.args.get('username')
    message = request.args.get('message')
    key = request.args.get('key')
    if key != VALID_KEY:
        return jsonify({'error': 'Mua key liên hệ tele @Dichvumxh307.'}), 403
    if not username or not message:
        return jsonify({'error': 'Missing username or message parameter'}), 400
    current_time = time.time()
    if username in ngl_log and current_time - ngl_log[username] < 30:
        return jsonify({'error': 'This username has been used recently. Please wait 30 seconds before trying again.'}), 429
    user_id = username
    stop_flag = threading.Event()
    STOP_FLAGS[user_id] = stop_flag
    user_locks[user_id] = threading.Lock()
    try:
        thread = threading.Thread(target=send_ngl_message, args=(username, message, user_id, stop_flag))
        thread.start()
        ngl_log[username] = current_time
        return jsonify({'message': f'NGL message sent to {username}. Please wait for completion.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def send_ngl_message(username, message, user_id, stop_flag):
    headers = {
        'Host': 'ngl.link',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0',
        'origin': 'https://ngl.link',
        'referer': f'https://ngl.link/{username}',
    }
    data = {
        'question': message,
        'username': username,
        'deviceId': '0',
        'gameSlug': '',
        'referrer': '',
    }
    for _ in range(30):
        if stop_flag.is_set():
            break
        try:
            response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error sending to NGL: {e}')
    with user_locks[user_id]:
        STOP_FLAGS.pop(user_id, None)
        user_locks.pop(user_id, None)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)