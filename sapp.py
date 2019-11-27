from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO 
from flask_socketio import send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_nums')
def update_nums():
    totnum = request.args.get('totnum')
    linenum = request.args.get('linenum')
    json = {'totnum': totnum, 'linenum': linenum} 
    emit('update', json, namespace="/test",broadcast=True) 
    return "true"

if __name__ == "__main__":
    socketio.run(app)
