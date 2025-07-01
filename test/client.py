#// Lib
from socket import *
#// data
host = 'localhost' #// host del servidor
port = 8000
#// node 
node = socket()
node.connect((host,port))

if __name__ == '__main__':
    node.close()
    pass