import socketio
import aiohttp
from aiohttp import web
import datetime
import time
from utils import Message
import utils
import db


sio = socketio.AsyncServer(max_http_buffer_size=10_000)
app = web.Application()
sio.attach(app)

database = db.DB("Messages",".")
database.connection = database.conn_db()
online_clients = dict()
#{sid:{acc_id:"",name:""}}

async def index(request):
    '''Serve the client side application.'''    
    with open('./files/index.html') as file:
        return web.Response(text=file.read(), content_type='text/html')
    
@sio.event
def connect(sid, environ):
    print(sid, "has connected to the server.")

@sio.event
async def disconnect(sid):
    print(f"{sid} has disconnected from the server.")

@sio.on('login')
async def login(sid, data):
    pass

@sio.on('search')
async def search(sid, data):
    '''
    data = {"query": "...}
    query.find('item')
    return a list of found items
    '''
    pass

@sio.on('create_project')
async def create_proj(sid, data):
    '''
    data = {
        "name": "project name",
        "description": "desc...",
        "tags": [],
        "collaborators":[],
        "image": {"name":"","content":bytearray}
    }
    save to files/images/projects/name.png
    remove image
    must generate room & table
    '''
    pass

@sio.on('chat_enter')
async def chat_enter(sid, room):
    await sio.enter_room(room)

@sio.on('chat_leave')
async def chat_leave(sid, room):
    await sio.leave_room(room)

@sio.on('chat_load')
async def chat_load(sid, data):
    '''
    returns a dict of list of chat log
    '''
    msgs = database.select_msgs(data["room_id"])
    msgs = utils.conv_from_msg(msgs)
    return msgs

@sio.on('chat')
async def chat(sid, data):
    '''
    returns a dict of chat
    '''
    dt = datetime.datetime.now()
    unix = time.mktime(dt.timetuple())
    msg = Message(0, data["client_id"], data["message"], unix)
    database.insert_msg(data["room_id"], msg)
    await sio.emit('chat', data, room=data["room_id"])


app.router.add_static('/static', './files')
app.router.add_get('/', index)

web.run_app(app, port=12121)