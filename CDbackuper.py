import os
from time import sleep

#check to see if the script has super user
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

filename = input('Input output image filename')
#un-mounts the drive incase it is already mounted
os.system('sudo umount /media/CDROM')
#creates a directory to mount the drive to
os.system('mkdir /media/CDROM')
#mounts the Drive under the Directory under /media/HDD
os.system('mount /dev/sr0 /media/CDROM')
#makes a disk image of the disk
os.system('sudo dd if= /dev/sr0 of= /home/alexander/Desktop/CDBUP/' + filename '.img bs=1k conv=noerror status=progress')
#exits the program
exit('\n \n \n \n \n \n \n \n \n Backup Complete')
