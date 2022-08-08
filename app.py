import datetime
from flask import Flask, render_template

app = Flask(__name__)


# def countdown():
#     while True:
#         difference

display_string = "<h3>It's coming for you!</h3> <br> <h1>30</h1>"


@app.route('/', methods=['GET'])
def display_countdown():

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
    print("App is running")
