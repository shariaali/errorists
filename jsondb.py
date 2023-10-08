import json
import random, string


def load_item(file:str):
    '''Loads all text from a json file.'''
    with open(file) as jsonfile:
        return json.load(jsonfile)
    
def update_file(file:str,data:dict):
    '''
    Rewrites the json file by dumping data into it.
    '''
    with open(file, 'w') as jsonfile:
        json.dump(data,jsonfile, indent=4)

def get_rand_id() -> str:
    '''
    Generates a random id for account and returns it.
    '''
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(2))
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    return id

#delete?
def all_online_clients(clients:dict, orig_sid) -> dict:
    '''
    Returns a dictionary containing details about all online clients.
    '''
    online_clients = {}
    online_clients["status"] = 2
    online_clients["clients"] = []
    for sid in clients:
        if sid == orig_sid:
            continue
        client_id = clients[sid]["online-id"]
        client_name = clients[sid]["name"]
        #online_clients["clients"].append({"name":client_name, "id":client_id}) ###to make 
    return online_clients

def add_project(file, data):
    #remove images here
    json_data = load_item(file)
    id:str
    while True:
        id = get_rand_id()
        if id in json_data:
            continue
        break
    img = f'./files/images/projects/{id}.png'
    with open(img, 'wb') as img_file:
        img_file.write(data["image"])

    del data['image']
    data['profile'] = img
    json_data[id] = data
    update_file(file, json_data)
    return id #returns an id for server to create table

def get_project(id, file):
    json_data = load_item(file)
    return json_data[id]

def add_account(file, data):
    json_data = load_item(file)
    id:str
    while True:
        id = get_rand_id()
        if id in json_data:
            continue
        break
    json_data[id] = data
    update_file(file, json_data)
    return id ##???

def get_account(id, file):
    json_data = load_item(file)
    return json_data[id]
