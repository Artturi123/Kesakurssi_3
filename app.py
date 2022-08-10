from app import db, Measurement
from flask import Flask

app = Flask(__name__)

@app.route("/")
def func():
    from models import db, Storage
    Measurement.query.all()
    return 

if __name__ == "__main__":
    app.run(debug=True)
    