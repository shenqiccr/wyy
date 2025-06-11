from flask import Flask
import keyboard

app = Flask(__name__)

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