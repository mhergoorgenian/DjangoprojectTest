"""Gunicorn configuration file for Django project."""

# Server socket
bind = "0.0.0.0:8000"

# Worker processes
workers = 4  # Recommended: 2-4 x $(NUM_CORES)
worker_class = "sync"
worker_connections = 1000
timeout = 30

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Logging
errorlog = "-"
loglevel = "info"
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = None

# Django WSGI application path
wsgi_app = "core.wsgi:application" 