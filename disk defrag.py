#!/usr/bin/env python
# coding: utf-8

# In[4]:


#disk defragmentation
drive=['C']
from subprocess import Popen,PIPE
import time
start=time.time()

def defrag(fragvol):
    print("Defragmentation......")
    fragment=Popen("defrag -u %s: "%fragvol,stdout=PIPE,stderr=PIPE,shell=True)
    res,err=fragment.communicate()
    if err:
        return err
    else:
        return res
    
for i in drive:
    defrag(i)
end=time.time()
print("Execution Time %s"%(end-start))
#Author Om Prakash

