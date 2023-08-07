import configparser, os
from playhouse.pool import PooledPostgresqlDatabase

config = configparser.ConfigParser()
config.read('config.ini')

env = os.environ.get('ENV', 'development')

db_host = config.get(env, 'DB_HOST')
db_user = config.get(env, 'DB_USER')
db_pass = config.get(env, 'DB_PASS')
db_name = config.get(env, 'DB_NAME')

db = PooledPostgresqlDatabase(
    user=db_user,
    password=db_pass,
    host=db_host,
    database=db_name,
    max_connections=8,
    stale_timeout=300
)
