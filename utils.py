from dataclasses import dataclass #mutable struct basically
from typing import NamedTuple #immutable struct basically

@dataclass
class Account:
    name:str
    desc:str
    skills:list
    projects:list
    rooms:list

@dataclass
class Room:
    id:str
    acc_ids:list
    admin:str

@dataclass
class Project:
    name:str
    id:int
    desc:str
    img:bytearray
    skills:list
    collaborators:list


class Message(NamedTuple):
    msg_id:int
    client_id:str
    message:str
    datetime:int

def conv_to_msg(msgs:list):
    to_return:list[Message]
    for item in msgs:
        msg = Message(item[0], item[1], item[2], item[3])
        to_return.append(msg)
    return to_return

def conv_from_msg(msgs:list[Message]):
    to_return:dict
    for item in msgs:
        to_return[item.msg_id] = {"client_id":item.client_id, "message":item.message, "datetime":item.datetime}
    return to_return