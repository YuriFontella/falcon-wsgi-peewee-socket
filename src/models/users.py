import peewee, uuid, datetime
from config.db.pool import db

class Users(peewee.Model):
    id = peewee.AutoField()
    name = peewee.CharField()
    group_id = peewee.IntegerField(index=True)
    uuid = peewee.UUIDField(default=uuid.uuid4)
    datetime = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db