import os


from hadoop import *
from LVMautomation import *
from aws import *
#from docker import *
from apache import *
from ansible import *

while True:
    os.system("clear")
   
    print("""    
    Press 1 for hadoop setup
    Press 2 for AWS 
    Press 3 to automate LVM Partitions
    Press 4 to setup docker
    Press 5 to configure Apache webserver in your system
    Press 6 for ansible configuration
    Press 7 to exit     
    """)

    print()
    option = input("Please enter your choice: ")
    
    if int(option) == 1:
        hadoop()
    elif int(option) == 2:
        aws()
    elif int(option) == 3:
        lvm()
    elif int(option) == 4:
        docker()
    elif int(option) == 5:
        apache()
    elif int(option) == 6:
        ansible()
    else:
        print("Thank you!")
        exit()
