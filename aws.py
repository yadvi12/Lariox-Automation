# Importing OS Module
import os

# This function will set the color of text to blue.
os.system("tput setaf 4")
def aws():

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                             AWS AUTOMATION                                   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    print(" ")
    
    while True:
        os.system("clear")
   
        print("""    
        Press 1 for configuring AWS
        Press 2 to create key-pair 
        Press 3 to create security-group
        Press 4 to launch an instance
        Press 5 to describe an instance
        Press 6 to create a volume in EBS
        Press 7 to attach an EBS volume to EC2 instance
        Press 8 to create a S3 Bucket
        Press 9 to exit
        """)

        print()
        op = input("Please enter your choice: ")

        if int(op) == 1:
            os.system("aws configure")
