import socketio

socket = socketio.Server(async_mode='eventlet', logger=True, cors_allowed_origins='*')
