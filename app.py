from flask import Flask
from prometheus_client import Counter, Summary

app = Flask(__name__)

# Create a metric to track request counts
REQUEST_COUNT = Counter('request_count', 'Request count')
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()  # Decorate function with metric.
def hello_world():
    REQUEST_COUNT.inc(1)
    return 'Hello, Radix!'
