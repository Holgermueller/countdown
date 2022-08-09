# import time
# import datetime
from flask import Flask, render_template

app = Flask(__name__)

name = "Bryan"


# def countdown(stop):
#     while True:
#         difference = stop - datetime.datetime.now()
#         count_hours, rem = divmod(difference.seconds, 3600)
#         count_minutes, count_seconds = divmod(rem, 60)
#         if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
#             count = '<h1>Time is up!!</h1>'
#             break
#         count = (str(difference.days) + " : " + str(count_hours) + " : " +
#                  str(count_minutes) + " : " + str(count_seconds))
#         return count


# end_time = datetime.datetime(2022, 8, 9, 0, 0, 0)
# display_time = countdown(end_time)


@app.route('/', methods=['GET'])
def display_countdown():
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run()
