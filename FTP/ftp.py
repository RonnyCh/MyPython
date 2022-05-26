

# https://www.devdungeon.com/content/python-ftp-client-tutorial#:~:text=FTP%20or%20File%20Transfer%20Protocol%20is%20a%20common,%28SFTP%29%20that%20uses%20SSH%20to%20encrypt%20the%20communication.


import ftplib
from ftplib import FTP_TLS
ftp = FTP_TLS('ccapaprod.planning-analytics.ibmcloud.com')
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()    # you have to run this otherwise won't work
# change dir
ftp.cwd("/prod/LCA/Upload Templates")
# list files
ftp.dir()






# Connect and login at once
with FTP_TLS(host='ccapaprod.planning-analytics.ibmcloud.com', user='FileShare', passwd='3KThy8DJpk6RWH') as ftp:
    #print(ftp.pwd())  # Usually default is /
        # For text or binary file, always use `rb`
    with open('test.txt', 'rb') as text_file:
        ftp.storlines('STOR test.txt', text_file)




LCA =  FTP_TLS(host='ccapaprod.planning-analytics.ibmcloud.com', user='FileShare', passwd='3KThy8DJpk6RWH') 


filenames = LCA.nlst() # get filenames within the directory
print filenames



print(LCA.cwd('prod/LCA')) 

LCA.dir()