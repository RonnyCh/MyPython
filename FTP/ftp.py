

# https://www.devdungeon.com/content/python-ftp-client-tutorial#:~:text=FTP%20or%20File%20Transfer%20Protocol%20is%20a%20common,%28SFTP%29%20that%20uses%20SSH%20to%20encrypt%20the%20communication.


import ftplib
from ftplib import FTP_TLS
ftp = FTP_TLS('ccapaprod.planning-analytics.ibmcloud.com')
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()    # you have to run this otherwise won't work
# change dir
#ftp.cwd("/prod/LCA/XeroImport/XeroExport/dist/api_output")
ftp.cwd("/prod/LCA/Upload Templates")
# list files
ftp.dir()
ftp.quit()

filename = 'demofile2.txt'

filename = 'NonFinancial Budget Upload.xlsx'

########### download file from FTP Server ##############
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp.retrbinary(f"RETR {filename}", file.write)


########## upload the file to FTP Server ###############
########## still not working ######################
ftp.set_debuglevel(2)
ftp.encoding = "utf-8"
with open(filename, "rb") as file:
    ftp.prot_p()    # you have to run this otherwise won't work
    # Command for Uploading the file "STOR filename"
    ftp.storbinary(f"STOR {filename}", file,1024)

########### delete a file ##########
ftp.delete('demofile2.txt')




###### trying without ftp ssl ######
from ftplib import FTP
from pathlib import Path

ftp = FTP('ccapaprod.planning-analytics.ibmcloud.com')

ftp = FTP_TLS()
ftp.connect('ccapaprod.planning-analytics.ibmcloud.com',21)
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()  
ftp.cwd("/prod/LCA/Upload Templates")
# list files
ftp.dir()

with FTP('ftpes://ccapaprod.planning-analytics.ibmcloud.com', 'FileShare', '3KThy8DJpk6RWH') as ftp, open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {file_path.name}', file)