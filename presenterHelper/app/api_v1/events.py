from .. import socketio

from flask import session, request
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


@socketio.on('update presentation', namespace='/test')
def update_presentation():

    print()





# @socketio.on('my event', namespace='/test')
# def test_message(message):
#
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': message['data'], 'count': session['receive_count']})
#
#
# @socketio.on('my broadcast event', namespace='/test')
# def test_broadcast_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': message['data'], 'count': session['receive_count']},
#          broadcast=True)
#
#
# @socketio.on('join', namespace='/test')
# def join(message):
#     join_room(message['room'])
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': 'In rooms: ' + ', '.join(rooms()),
#           'count': session['receive_count']})
#
#
# @socketio.on('leave', namespace='/test')
# def leave(message):
#     leave_room(message['room'])
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': 'In rooms: ' + ', '.join(rooms()),
#           'count': session['receive_count']})
#
#
# @socketio.on('close room', namespace='/test')
# def close(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
#                          'count': session['receive_count']},
#          room=message['room'])
#     close_room(message['room'])
#
#
# @socketio.on('my room event', namespace='/test')
# def send_room_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': message['data'], 'count': session['receive_count']},
#          room=message['room'])
#
#
# @socketio.on('disconnect request', namespace='/test')
# def disconnect_request():
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': 'Disconnected!', 'count': session['receive_count']})
#     disconnect()