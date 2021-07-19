#Remove windows app all users in windows 10
#check using below comannd to know which apps you need to uninstall        
#print(os.popen('powershell "Get-AppxPackage -AllUsers | Select Name"').read())
ls=["king.com.FarmHeroesSaga"]
import os
import time
import datetime
from subprocess import PIPE,Popen

dat=datetime.date.today()
print("Date: %s"%dat)
start=time.time()
def execution(command):
    p=Popen(command,stdout=PIPE,stderr=PIPE)
    res,err=p.communicate()
    if err:
        print(err)
    else:
        if len(res.decode("utf-8"))==0:
            print("Successfully Removed")
        else:
            print(res)            
pack_to_unistall=['powershell "Get-AppxPackage -Name %s -AllUsers | Remove-AppxPackage -AllUsers"'%i for i in ls]
print(os.popen('powershell "Set-ExecutionPolicy RemoteSigned"').read())
for i in pack_to_unistall:
    execution(i)
end=time.time()
print("Execution Time : %s"%(end-start))
#Author OmPrakash