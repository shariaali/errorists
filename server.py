import socketio
import aiohttp
from aiohttp import web

<<<<<<< Updated upstream
sio = socketio.AsyncServer(max_http_buffer_size=1_000_00)
=======

sio = socketio.AsyncServer(max_http_buffer_size=100_000_000)
>>>>>>> Stashed changes
app = web.Application()
sio.attach(app)


async def index(request):
    '''Serve the client side application.'''
    
    with open('./files/index.html') as file:
        return web.Response(text=file.read(), content_type='text/html')
    
@sio.event
def connect(sid, environ):
    print(sid, "has connected to the server.")
    environ = ""

@sio.event
async def disconnect(sid):
    print(f"{sid} has disconnected from the server.")

<<<<<<< Updated upstream
=======
@sio.on('login')
async def login(sid, data):
    accs = jsondb.load_item("accs.json")
    acc_id = ""
    for key in accs:
        if accs[key]["username"] == data["username"] and accs[key]["password"] == data["password"]:
            acc_id = key
            online_clients[sid] = {"acc_id":acc_id, "name":data["username"]}
    await sio.emit('logged_in', True, to=sid)


@sio.on('signup')
async def signup(sid, data):
    print("SIgnup")
    accs = jsondb.load_item('accs.json')
    id:str
    while True:
        id = jsondb.get_rand_id()
        if id in accs:
            continue
        break
    accs[id] = {"username":data["username"], "password":data["password"]}
    jsondb.update_file('accs.json', accs)


@sio.on('logout')
async def logout(sid):
    del online_clients[sid]


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
        "tags": skill,
        "collaborators":[],
        "image": bytearray,
    }
    '''
    table_id = jsondb.add_project("projects.json", data)
    print("Added project to database.")
    database.create_table(table_id)
    print("Added room to database.")
    await sio.emit('create_project', True, to=sid)

@sio.on('load_project')
async def load_proj(sid, id):
    project = jsondb.get_project(id,"projects.json")
    await sio.emit('load_project', project, to=sid)
    
@sio.on('load_projects')
async def load_proj(sid):
    project = jsondb.load_item("projects.json")
    sio.emit('get_projects', project, to=sid)


@sio.on('chat_enter')
async def chat_enter(sid, room):
    sio.enter_room(sid, room)

@sio.on('chat_leave')
async def chat_leave(sid, room):
    sio.leave_room(sid, room)

@sio.on('chat_load')
async def chat_load(sid, data):
    '''
    returns a dict of list of chat log
    '''
    msgs = database.select_msgs(data["room_id"])
    msgs = utils.conv_from_msg(msgs)
    
    sio.enter_room(sid, data['room_id'])
    await sio.emit('chat_load',data=msgs,room=data['room_id'])
    print(msgs)

@sio.on('chat')
async def chat(sid, data):
    '''
    returns a dict of chat
    '''
    print(data)
    dt = datetime.datetime.now()
    unix = time.mktime(dt.timetuple())
    msg = Message(0, data["client_id"], data["message"], unix)
    database.insert_msg(data["room_id"], msg)
    await sio.emit('chat', data, room=data["room_id"])


>>>>>>> Stashed changes
app.router.add_static('/static', './files')
app.router.add_get('/', index)

web.run_app(app, port=12121)