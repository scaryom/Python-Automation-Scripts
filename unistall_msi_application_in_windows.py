#Teseted on windows 10
#Make Sure have admin right to remove application

msi_application_name="Autodesk Single Sign On Component"
from subprocess import Popen,PIPE
import time
import os
start=time.time()
cmd="""wmic product where 'Name like "%{}%"' get name,identifyingnumber""".format(msi_application_name)
apps=os.popen(cmd).read()
try:
    app=apps.splitlines()[2].split()[0]
    cmd2="""msiexec /x {} REBOOT=ReallySuppress /qn""".format(app)
    obj=Popen(cmd2,stdout=PIPE,stderr=PIPE)
    res,err=obj.communicate()
    if err:
        print(err)
    else:
        print("Successfully Remvoved %s"%msi_application_name)
    
except:
    print("Given Application doesn't exist")


end=time.time()
print("Execution Time : %s"%(end-start))
#Author Om Prakash