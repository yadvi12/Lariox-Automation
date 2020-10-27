#from dealtalfa import *
#from digambar import *
#from yadvi import *
#from skyhigh import *
import platform as pl
import os 

def myfunction():
    print("Os is " + pl.system())
    
    print("------------------------------------------------------")
    while(True):
        print("""
        1:-AWS service \t\t 2:-Hadoop service \t\t 3:-Gcp servie \n\n\t 4:-Docker \t\t 5:-exit  
        """)
        user_service=(input("Enter service number")).lower()
        if (user_service=='1' or 'aws' in user_service):
                print("Aws")
                input("Enter to continue")
                os.system("cls")
                #aws()
    
        if (user_service=='2' or 'hadoop' in user_service):
                print("Hadoop")
                input("Enter to continue")
                os.system("cls")
                #hadoop()

        if (user_service=='3' or 'gcp' in user_service):
                print("GCP")
                input("Enter to continue")
                os.system("cls")
                #gcp()
            
            
        if (user_service=='4' or 'docker' in user_service):
                print("docker")
                input("Enter to continue")
                os.system("cls")
                #docker()
                
                
        if (user_service=='5' or "exit" in user_service):
            print("Bye")
            break

if __name__=='__main__':
    myfunction()