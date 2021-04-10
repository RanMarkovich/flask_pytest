from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return 'hello_flask', 200


app.run(host='0.0.0.0', debug=True)
