
### checking file stats

import os
import datetime

## st_atime => Last File Access Time
## st_mtime => Last File Modification Time
## st_ctime => File Creation Time

stats = os.stat('cbahome.csv')
print(stats.st_atime)               # Prints out 1615950895.8777606
print(stats.st_mtime)               # Prints out 1615950893.747034
print(stats.st_ctime)               # Prints out 1615950894.7286537

date_object_st_atime = datetime.datetime.fromtimestamp(stats.st_ctime)
date_object_st_mtime = datetime.datetime.fromtimestamp(stats.st_mtime)
date_object_st_ctime = datetime.datetime.fromtimestamp(stats.st_ctime)

print("Last time file was accesses => ", date_object_st_atime)
print("Last time file was Modified => ", date_object_st_mtime)
print("File was created => ", date_object_st_ctime)


## test code ronny ##

if stats.st_mtime < time.time():
    print ('OK')