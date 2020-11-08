# Importing OS Module
import os

# This function will set the color of text to blue.
os.system("tput setaf 4")
def apache():

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                             CONFIGURATION OF WEB-SERVER USING APACHE                                   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(" ")
    print("NOTE: Make sure that yum is configured in your system.")
    print(" ")
    os.system("yum install httpd")
    os.system("setenforce 0")
    os.system("systemctl stop firewalld")
    os.system("systemctl start httpd")
    choice = input("Do you want to launch a webpage on this webserver: Yes or No :  ")
    choice = choice.lower()
    if choice == "yes":
        filename = input("Tell us the name of the file: ")
        location = input("Location of the file: ")
        os.system("cp  {0}{1}  /var/www/html".format(location,filename))
        input("The webserver is successfully configured. Press Enter to continue.")
    else:
        print("Thank you!")
        input("The webserver is successfully configured.Press Enter to continue.")
        exit()


