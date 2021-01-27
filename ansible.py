# Importing OS Module
import os
import getpass
# This function will set the color of text to blue.
#os.system("tput setaf 4")
def ansible():

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                             ANSIBLE AUTOMATION                                   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")

    while True:
        os.system("clear")

        print("""    
        Press 1 for configuring Ansible in your system
        Press 2 for configuration management using ansible
        Press 3 to exit
        """)

        print()
        op = input("Please enter your choice: ")

        if int(op) == 1:
            print("Make sure epel and yum is configured in your system")
            print()
            os.system("pip3 install ansible")
            os.system("yum install sshpass -y")
            os.system("touch /root/ip.txt")
            os.system("mkdir /etc/ansible")
            os.system("touch /etc/ansible/ansible.cfg")
            f=open("/etc/ansible/ansible.cfg","w")
            f.write("""[defaults] \ninventory = /root/ip.txt \nhost_key_checking=false \ndeprecation_warnings=False""")
            target = input("How many target nodes you want to configure: ")
            i = 0
            s = "Enter IP "
            c = ": "
            while i < int(target):
                ip = input(s + str(i+1) + c)
                user = input("Enter username: ")
                pwd = getpass.getpass("Enter password: ")
                p = open("/root/ip.txt", "a")
                p.write(ip + " ansible_user=" + user + " ansible_ssh_pass=" + pwd + " ansible_connection=ssh\n")
                p.close()
                i =i + 1
            print("Ansible is successfully configured in your system, if you want to test it, run ansible all --list host command.")
            input("Press enter key to continue")
        elif int(op) ==2:
            os.system("clear")
            print("Please make sure that ansible and yum is configured in your system.") 
            print(""" 
                      Press 1 to configure load balancer for the web-servers
                      Press 2 to configure yum in your system
                      Press 3 to configure web-server(it will also configure yum repo)
                      Press 5 to exit
                  """)
            print()
            opt = input("Please enter your choice: ")
            if int(opt) == 1:
                iplb = input("Please enter the IP of load balancer: ")
                lbu = input("Enter username: ")
                lbp = getpass.getpass("Enter password: ")
                q = open("/root/ip.txt", "a")
                q.write("[mylb]\n" + iplb + " ansible_user=" + lbu + " ansible_ssh_pass=" + lbp + " ansible_connection=ssh\n")
                q.close()
                ipws = input("How many webservers you want to attach to the load balancer: ")
                i = 0
                s = "Enter IP "
                c = ": "
                while i < int(ipws):
                    ip = input(s + str(i+1) + c)
                    user = input("Enter username: ")
                    pwd = getpass.getpass("Enter password: ")
                    p = open("/root/ip.txt", "a")
                    p.write("[myweb]\n")
                    p.write(ip + " ansible_user=" + user + " ansible_ssh_pass=" + pwd + " ansible_connection=ssh\n")
                    p.close()
                    i =i + 1

                os.system("ansible-playbook setup.yml")
                print("Load-Balancer is been successfully configured in your system, you can try accessing the IP of your load-balancer.")
                input("Press enter key to continue") 
            elif int(opt) == 2:
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
                 input("Press enter key to continue")
            elif int(opt) == 3:
                nweb = input("how many systems you want to configure as web-servers: ")
                i = 0
                s = "Enter IP "
                c = ": "
                while i < int(nweb):
                    ip = input(s + str(i+1) + c)
                    user = input("Enter username: ")
                    pwd = getpass.getpass("Enter password: ")
                    p = open("/root/ip.txt", "a")
                    p.write("[webpreq]\n")
                    p.write(ip + " ansible_user=" + user + " ansible_ssh_pass=" + pwd + " ansible_connection=ssh\n")
                    p.close()
                    i = i+1
                os.system("ansible-playbook web-preq-dynamic.yml")
                print("Web-server is successfully configured on port 80")
                input("Press enter key to continue")
            elif int(opt) == 5:
                exit()

        elif int(op) == 3:
            exit()
