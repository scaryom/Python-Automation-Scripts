#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Tested in windows 10
#File which accessed won't be removed
#python3.7
import os
import time
import shutil
start=time.time()
permission=lambda path:os.chmod(path,777)
users=os.popen("net user").read().split()[5:-4]
for i in users:
    path="C:\\Users\\%s\\AppData\\Local\\Temp"%i
    if os.path.exists(path):
        print(path)
        permission(path)
        shutil.rmtree(path,ignore_errors=True)
end=time.time()
print("Execution Time %s "%(end-start))
#Author OM

