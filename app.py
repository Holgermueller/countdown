import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def countdown():
    present = datetime.datetime.now()
    future = datetime.datetime(2023, 3, 9)
    difference = future - present
    return str(difference)


if __name__ == "__main__":
    app.run()
    print("App is running")
