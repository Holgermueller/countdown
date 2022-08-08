import time
import datetime
from flask import Flask, render_template

app = Flask(__name__)

name = "Bryan"


def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            return '<h1>Time is up!!</h1>'
        time.sleep(1)
        return (str(difference.days) + " days(s) " + str(count_hours) + " hour(s) " + str(count_minutes) + " minute(s) " + str(count_seconds) + " second(s)")


end_time = datetime.datetime(2022, 8, 9, 0, 0, 0)


display_time = countdown(end_time)


@app.route('/', methods=['GET'])
def display_countdown():

    return render_template("index.html", name=name, display_time=display_time)


if __name__ == "__main__":
    app.run()
