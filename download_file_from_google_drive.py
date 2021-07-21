URL="https://docs.google.com/document/d/1GQZZAleRzBTnEEXVqJ3REwcpFNg1EYLQTw5rDeuz94g/export?format=pdf"#Direct Download LInk
file_name="para.doc"#File with extension
destination="F:\\"#Path

import os
import requests
import time
start=time.time()
f_destination=os.path.join(destination,file_name)
response=session.get(URL,stream = True)
size=5000
with open(f_destination,"wb") as f1:
    for i in response.iter_content(size):
        f1.write(i)
end=time.time()
print("Execution Time : %s"%(end-start))
#Author Om Prakash