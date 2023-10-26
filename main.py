import os
import time
while 1:
    os.system('ping 8.8.8.8 -n 1') #change "8.8.8.8" to the ip of the server you would like to test your ping to.
    time.sleep(3) #you can change this value to make it ping less or more frequently, making the value lower should not lower your internet or system speed by any means. 