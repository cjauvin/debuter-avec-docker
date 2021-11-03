from flask import Flask
import redis

app = Flask(__name__)

red = redis.Redis("db")
KEY = "some_key"

@app.route("/set/<val>")
def set_value(val):
    red.set(KEY, val)
    return f"Your value ({val}) is now set in the database"

@app.route("/get")
def get_value():
    val = red.get(KEY)
    if val is None:
        return "No value was stored, use /set"
    return f"Your stored value is {val}"
