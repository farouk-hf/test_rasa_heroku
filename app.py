from flask import Flask
from model_manager import ModelManager
app = Flask(__name__)

@app.route('/')
def homepage():
    inter = ModelManager.load_exisiting_model('./model_dir/model_20170606-173115')
    return inter.parse("hi ich will Informatik studieren")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

