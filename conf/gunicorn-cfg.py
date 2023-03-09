"""Config for the gunicorn web server that serves the flask app."""
import os

# there are more variables that it is possible to set; these are the ones i imagine we might want to change easily or
#   often enough to warrant including as env var config
# https://docs.gunicorn.org/en/stable/settings.html
bind = os.getenv('GUNICORN_BIND_ADDRESS', '0.0.0.0:5000')
backlog = os.getenv('GUNICORN_MAX_NUM_PENDING_CONNS', 2048)
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'sync')
workers = os.getenv('GUNICORN_NUM_WORKERS', 2)
threads = os.getenv('GUNICORN_NUM_THREADS_PER_WORKER', 1)
worker_connections = os.getenv('GUNICORN_MAX_SIMULTANEOUS_CLIENTS', 1000)  # only affects certain worker types
max_requests = os.getenv('GUNICORN_MAX_REQUESTS', 0)  # setting to positive int forces worker restart after that many
max_requests_jitter = os.getenv('GUNICORN_MAX_REQUESTS_JITTER', 0)
timeout = os.getenv('GUNICORN_WORKER_TIMEOUT', 30)
graceful_timeout = os.getenv('GUNICORN_WORKER_GRACEFUL_TIMEOUT', 30)
keepalive = os.getenv('GUNICORN_SECS_WAIT_ON_KEEPALIVE', 2)  # note, sync worker does not support keepalive
