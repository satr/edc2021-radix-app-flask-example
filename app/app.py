from flask import Flask
import logging

logging = logging.getLogger('app')
logging.setLevel(logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Radix!'

# Metrics endpoint
@app.route('/job1')
def run_job1():
    logging.info('Running job1')
    return 'run job1'
