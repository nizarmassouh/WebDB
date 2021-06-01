import numpy as np
import cv2

p=open("path.txt") #file to all image paths
o=open("isolated.txt",'w') #file to write to the isolated images' paths
isolated=[]
for im in p:
    I=cv2.imread(im.rstrip())
    c=0
    w=0
    for i in I:
        for j in i:
            c+=1
            if (255 - np.mean(list(j))) <= 10:
                w+=1
    t=float(w)/float(c) *100
    if t>=30:
        isolated.append(im)

for i in isolated:
    o.write(i)

