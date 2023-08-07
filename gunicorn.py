import multiprocessing, os

from config.migrations.main import create_tables

cpus = multiprocessing.cpu_count()

bind = '0.0.0.0:8000'
workers = int(cpus / 2) + 1
threads=cpus * 2
wsgi_app = 'src.app:wsgi'
worker_class='eventlet'
loglevel = 'info'
chdir=os.path.dirname(os.path.abspath(__file__))
timeout=300
limit_request_line=8188

reload = True

def when_ready(server):
    create_tables()