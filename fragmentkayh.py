print("""
  _  __              _    _    _____  _   _   _____ 
 | |/ /             | |  | |  / ____|| \ | | / ____|
 | ' /  __ _  _   _ | |__| | | |  __ |  \| || |  __ 
 |  <  / _` || | | ||  __  | | | |_ || . ` || | |_ |
 | . \| (_| || |_| || |  | | | |__| || |\  || |__| |
 |_|\_\\\__,_| \__, ||_|  |_|  \_____||_| \_| \_____|    
               __/ |                                
              |___/                                       
      
           Github: https://github.com/kayhgng
""")

config_tempklate = """"
https://fragment.first-to-the-egg.workers.dev/frag/ip/[worker]/uuid/host/port/path
"""

worker = input("Please Enter your worker's address without htttps and /:")
uuid = input("Please Enter your uuid:")
host = input("Please enter the host name:")
port = input("Please Enter your host's port:")
path = input("Please Enter your path :") 

subsctiption = config_tempklate.replace("[worker]", worker).replace("uuid", uuid).replace("host", host).replace("port", port).replace("path", path)

print("[Here is your subscription Group url:")
print (subsctiption)
