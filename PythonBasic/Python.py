
# change directory so it will pick up your module
import os
os.chdir(r'c:\\Users\r.christianto\MyPython\PythonBasic')

# simple module with two definitions inside
import Module as x
x.calc(10)




############# create dict from list #######################
name = ['ronny','mercedes','other']
love = [0,1]
hate = [100,100]

mydict = dict(zip(name,love,hate))

for i in mydict:
    print (mydict[i])


list(mydict)[0]   

for i in (1,2):
    print (name[i])


############### diff between break and continue ##############

for i in range(1,10):
    if i < 8:
        print (i)
    else:
        break # it will stop loop all together
        print (' this will not print')


for i in range(1,10):
    if i < 8:
        print (i)
    else:
        continue # it will stop here and continue next loop
        print (' this will not print')

