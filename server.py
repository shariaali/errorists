import socketio
import aiohttp
from aiohttp import web

sio = socketio.AsyncServer(max_http_buffer_size=1_000_00)
app = web.Application()
sio.attach(app)


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

app.router.add_static('/static', './files')
app.router.add_get('/', index)

web.run_app(app, port=12121)