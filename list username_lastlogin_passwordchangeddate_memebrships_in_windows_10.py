#Tested In WIndows10(32bit and 64 bit)
#LocalSystem 
import os
import time
start=time.time()

users=os.popen("net user").read()
#fil_users=[i for i in users.split()[5:-4] if i!='Administrator' and i!='Guest']
for i in users.split()[5:-4]:
    size=len(i)+11
    print("-"*size)
    print "User Name: "+i+" \n"+"-"*size
    print os.popen('net user  "%s" | findstr /B /C:"Last logon"'%i).read()
    print os.popen('net user  "%s" | findstr /B /C:"Password last set"'%i).read()
    print os.popen('net user  "%s" | findstr /B /C:"Local Group Memberships"'%i).read()

end=time.time()
print("-"*40)
print"Execution Time %s "%(end-start)
#Author OM PRAKASH