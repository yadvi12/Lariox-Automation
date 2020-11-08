# Importing OS Module
import os

# This function will set the color of text to blue.
os.system("tput setaf 4")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                             LVM PARTITIONS USING PYTHON AUTOMATION                                   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print(" ")
number = input("How many hard-disks you want to attach to the LVM partition-  ")

i=0
s=" "
num_array = list()
while i<int(number):
    name = input("Name of the hard-disk: ")
    num_array.append(name)             # Creating an array to store all the values which user will input in the name variable.
    i=i+1
    os.system("pvcreate {}".format(name))    # This command will configure the hard-disks as physical volumes.
s = s.join(num_array)                        # Joining the list items of num_array with space.
volumegrp = input("Name you want to give to the volume group:  ") 
os.system("vgcreate {} {}".format(volumegrp,s))  # Creating a volume group of all the physical volumes.

print(" ")
print("Voila!,the volume group is successfully created, now it's the time to create a logical volume.")
print("NOTE: The size should be less than the total capacity of all the hard-disks you added.") 
print(" ")   

lv_name=input("Please specify the name of the logical volume or physical partition you want to create: ")
lv_size=input("Now tell us the size in GB: ")
os.system("lvcreate --size {}GB --name {} {}".format(lv_size,lv_name,volumegrp))         # Creating logical volume.
os.system("mkfs.ext4 /dev/"+volumegrp+"/"+lv_name)                                       # Formating the partition.
mount_folder=input("Specify the mount point of the LVM(i.e. a folder where you want to mount your partition): ")
os.system("mount /dev/"+volumegrp+"/"+lv_name+"  "+mount_folder)                         # Mounting the partition on the folder specified by the user.
print("Tada!, logical volume is successfully created, formatted and mounted on the folder " + mount_folder + ".")
    


         
