import datetime
from flask import Flask, render_template

app = Flask(__name__)


# def countdown():
#     while True:
#         difference

name = "Bryan"


@app.route('/', methods=['GET'])
def display_countdown():

    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run()
    print("App is running")
