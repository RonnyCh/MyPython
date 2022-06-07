

# https://www.devdungeon.com/content/python-ftp-client-tutorial#:~:text=FTP%20or%20File%20Transfer%20Protocol%20is%20a%20common,%28SFTP%29%20that%20uses%20SSH%20to%20encrypt%20the%20communication.

import os
import ftplib
from ftplib import FTP_TLS
ftp = FTP_TLS('ccapaprod.planning-analytics.ibmcloud.com')
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()    # you have to run this otherwise won't work
# change dir
ftp.cwd("/prod/LCA/XeroImport/XeroExport/dist/api_output")
#ftp.cwd("/prod/LCA/Upload Templates")
# list files
ftp.dir()
ftp.quit()

# chdir
os.chdir(r'C:\Users\r.christianto\MyPython\FTP')


########### download file from FTP Server ##############
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp.retrbinary(f"RETR {filename}", file.write)




########## upload the file to FTP Server ###############
########## finallly working ######################
filename = 'TrialBalance_2022-05-31_2022-05-31.txt'
#ftp.set_debuglevel(2)
ftplib._SSLSocket = None   #### this is key to make upload work!!!! (from reza code)
with open(filename, "rb") as file:
    ftp.prot_p()    # you have to run this otherwise won't work
    # Command for Uploading the file "STOR filename"
    ftp.storbinary(f"STOR {filename}", file,1024)



########### delete a file ##########
ftp.delete(filename)
ftp.dir()

