from flask import Flask

app = Flask(__name__)

@app.route("/data")
def hello():
    data = dict()
    data['balance'] = list(range(5))
    data['interest'] = [0.1]*5
    data['payment'] = [0.2]*5
    return str(data)

if __name__ == "__main__":
    app.run()
