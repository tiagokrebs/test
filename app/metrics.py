import time
import flask
from prometheus_client import Counter, Histogram
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

REQUEST_COUNTER = Counter('app_requests_total', 'Total number of requests to the application')
REQUEST_TIME = Histogram('request_duration_seconds', 'Duration of requests')

def increment_request_counter():
    REQUEST_COUNTER.inc()

def observe_request_time(duration):
    REQUEST_TIME.observe(duration)

def setup_metrics(app):
    # Add prometheus wsgi middleware to route /metrics requests
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    @app.before_request
    def before_request():
        increment_request_counter()
        flask.g.start_time = time.time()  # Use the time module

    @app.after_request
    def after_request(response):
        total_request_time = time.time() - flask.g.start_time  # Use the time module
        REQUEST_TIME.observe(total_request_time)
        return response
