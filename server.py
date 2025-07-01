#// Lib
from socket import *
import asyncio as asyn
from core.user import *

#// function
async def client(conection):
    name = user_name()

if __name__ == '__main__':
    print("[*] Starting server")
    #// configuracion de node
    try:
        node = socket(AF_INET,SOCK_STREAM)
        node.bind(('localhost',8000))
        node.listen(15)
        while True:
            conection,addr = node.accept()
            asyn.run(client(conection))
    except error as err:
        print("[*] Internal server error:")
        print(f"[*] {err}")
    #//
    pass