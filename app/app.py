import time
from flask import (
    Flask, render_template
)
import schedule
import threading
import logging
import traceback

# https://docs.python.org/3/howto/logging.html
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# add ch to logger
logger.addHandler(ch)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

app = Flask(__name__)

app.logger.addHandler(ch)
app.logger.setLevel(logging.DEBUG)
app.logger.debug("Started app debug")
app.logger.info("Started app info")
app.logger.error("Started app error")

counter = 0  # counter to immitate regular error in the job


# job, running by the scheduler
def job():
    try:
        app.logger.info("I'm working...")
        # example of an exception - every 3rd job run
        global counter
        counter = counter - 1
        if counter <= 0:
            counter = 3
            1 / 0
    except:
        app.logger.error("Exception: {}".format(traceback.format_exc()))


# https://schedule.readthedocs.io/en/stable/background-execution.html
schedule.every(3).seconds.do(job)


# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

def run_continuously(interval=3):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


stop_run_continuously = run_continuously()


@app.route('/')
def status():
    if stop_run_continuously is None:
        return render_template('view.html', message='Job scheduler is stopped')
    return render_template('view.html', message='Job scheduler is running')


@app.route('/start')
def start_job_scheduler():
    global stop_run_continuously
    if stop_run_continuously is not None:
        return render_template('view.html', message='Job scheduler already started')
    stop_run_continuously = run_continuously()
    return render_template('view.html', message='Started job scheduler')


@app.route('/stop')
def stop_job_scheduler():
    global stop_run_continuously
    stop_run_continuously.set()
    stop_run_continuously = None
    return render_template('view.html', message='Stopped job scheduler')
