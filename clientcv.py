#%%
import cv2
import numpy as np
from networkcv import Network
from callcv import Call                         
    
import sys
def main():
    run=True
    n=Network()
    p=int(n.getP())
    print("You are participant ",p+1)
    myvid=cv2.VideoCapture(0)
    myvid.set(3,640)
    myvid.set(4,480)
    myvid.set(10,100)
    while run:
        callvid=0
        try:
            print('sent')
            success,img = myvid.read()
            print(success)
            img_str = cv2.imencode('.jpg', img)[1].tostring()
            print("size:", sys.getsizeof(img_str))
            nparr = np.fromstring(n.send(img_str), np.uint8)
            print(sys.getsizeof(nparr))
            callvid = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        except Exception as e:
            print(e)
            run=False
            print(f"Cutting call...Participant {(p+1)%2+1} left")
            break
        cv2.imshow("VideoCall", callvid)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            run=False
            
            
        
if __name__=="__main__":
    main()
    