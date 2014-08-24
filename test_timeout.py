"""
To test timeout::

    $ python test_timeout.py &
    $ python
    >>> import requests
    >>> # should raise timeout exception
    >>> requests.get('http://localhost:8888', timeout=1.0)
"""

import time
import flask
from flask import Flask, Response

app = Flask(__name__)

def serve():
    while True:
        time.sleep(0.5)
        yield 'a'

@app.route('/')
def index():
    return Response(serve(), mimetype='text/plain')

if __name__ == '__main__':
    app.debug = True
    app.run(port=8888)