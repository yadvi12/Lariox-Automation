import os
#import pyttsx3

#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#rate = engine.getProperty('rate')
#engine.setProperty('rate', 125)


from hadoop import *
from LVMautomation import *
#from aws import *
#from docker import *
from apache import *
from ansible import *

while True:
    os.system("clear")
    print(""" ************  LARIOX AUTOMATION  ************* """)
 #   pyttsx3.speak("Greetings, this is Lariox, a personal voice assistant for linux based automated tasks.") 
    print("""    
    Press 1 for hadoop setup
    Press 2 for AWS 
    Press 3 to automate LVM Partitions
    Press 4 for docker configuration
    Press 5 to configure Apache webserver in your system
    Press 6 for ansible configuration
    Press 7 to configure yum  
    Press 8 to exit the program
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
    elif int(option) == 7:
                 yumc = input("In how many systems you wanna configure yum: ")
                 l = 0
                 s = "Enter IP "
                 c = ": "
                 while l < int(yumc):
                    ip = input(s + str(l+1) + c)
                    user = input("Enter username: ")
                    pwd = getpass.getpass("Enter password: ")
                    p = open("/root/ip.txt", "a")
                    p.write("[yumpreq]\n")
                    p.write(ip + " ansible_user=" + user + " ansible_ssh_pass=" + pwd + " ansible_connection=ssh\n")
                    p.close()
                    l = l+1
                 os.system("ansible-playbook yum.yml")
                 print("Yum is successfully configured in your system")
                 input("Press enter to continue")
    else:
        print("Thank you!")
        exit()
