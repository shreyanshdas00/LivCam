#%%
import socket
from _thread import *
import pickle
import numpy as np
from callcv import Call
import sys
#import cv2

server="192.168.1.13"
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)
    
s.listen(2)#2=max number of clients
print("Waiting for a connection, Server Started")

calls={}
idCount=0

def threaded_client(conn,p,callId):
    global idCount
    conn.send(str(p).encode("utf-8"))
    while True:
        data = None
        try:
            data = conn.recv(143360)
            print(sys.getsizeof(data))
            if callId in calls:
                call=calls[callId]
                
                if not(data):
                    print("Disconnected: ", p+1)
                    break
                else:
                    call.set_vid(p, data)
                    conn.send(call.get_vid(p))
            else:
                break
        except:
            break
        
    print(f"Participant {p+1} left")
    try:
        del calls[callId]
        print("Cutting call: ",callId)
    except:
        pass
    idCount-=1
    conn.close()

if __name__=="__main__":            
    while True:
        conn,addr=s.accept()
        print("Connected to: ",addr)
        idCount+=1
        p=0
        callId=(idCount-1)//2
        if idCount%2==1:
            calls[callId]=Call(callId)
            print("Placing new call")
        else:
            calls[callId].ready=True
            p=1
        start_new_thread(threaded_client,(conn,p,callId))
    
#%%
import numpy as np
n=np.random.rand(480,640,3)
print("%d bytes" % (n.size * n.itemsize))
