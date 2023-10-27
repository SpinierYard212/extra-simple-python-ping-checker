import os
import time
server=input("enter server")
while 1:
    os.system(f'ping {server} -n 1') #change "8.8.8.8" to the ip of the server you would like to test your ping to.
    time.sleep(3) #you can change this value to make it ping less or more frequently, making the value lower should not lower your internet or system speed by any means. 
