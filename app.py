from datetime import datetime

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    val_return = "Current\tdatetime\t(UTC):\t{}".format(str(datetime.utcnow())) 
    return val_return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)