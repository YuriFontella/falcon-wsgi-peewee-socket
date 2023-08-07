from src.models.users import Users
from config.db.pool import db

def create_tables():
    with db:
        db.create_tables([Users])
