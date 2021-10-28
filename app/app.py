from flask import Flask
from prometheus_client import Counter, Summary, generate_latest

app = Flask(__name__)

# Create a metric to track request counts
REQUEST_COUNT = Counter('custom_request_count', 'Request count')
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('custom_request_processing_seconds', 'Time spent processing request')


@app.route('/')
@REQUEST_TIME.time()  # Decorate function with metric.
def hello_world():
    REQUEST_COUNT.inc(1)
    return 'Hello, Radix!'

# Metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_latest()
