#%%
import numpy as np
import cv2
class Call:
    def __init__(self,id):
        self.ready=False
        self.id=id
        default_img = np.zeros((480,640,3))
        default_screen = cv2.imencode('.jpg', default_img)[1].tostring()
        self.vids=[default_screen, default_screen]
        
    def connected(self):
        return self.ready
    
    def get_vid(self,p):
        return self.vids[(p+1)%2]
    
    def set_vid(self,p,vid):
        self.vids[p]=vid
        