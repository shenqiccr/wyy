from flask import Flask
from flask_cors import CORS
import keyboard

app = Flask(__name__)
CORS(app)  # 允许所有跨域请求

@app.route('/playpause')
def playpause():
    keyboard.send('ctrl+alt+p')
    return 'ok'

@app.route('/next')
def next_song():
    keyboard.send('ctrl+alt+right')
    return 'ok'

@app.route('/prev')
def prev_song():
    keyboard.send('ctrl+alt+left')
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
