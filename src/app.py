import falcon, socketio

from src.middlewares.auth import Auth
from src.middlewares.pool import Pool
from src.socket.server import socket

from src.controllers import  users

app = falcon.App(middleware=[Pool(), Auth()])

users = users.UsersResource()

app.add_route('/users', users)
app.add_route('/users/{id}', users, suffix='user')

wsgi = socketio.WSGIApp(socket, app)
