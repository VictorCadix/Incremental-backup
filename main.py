import shutil
import os
from pathlib import Path
import filecmp
import backupFunctions as bckp

dir2Backup = "C:/Users/victo/Desktop/Server"
backupDir = "C:/Users/victo/Desktop/BackupServer"

server_dirs = os.listdir(dir2Backup)
print('folderContent')
for i in server_dirs:
    print('\t' + i)


dirs = os.listdir(backupDir)
print('Destination files:')
for i in dirs:
    print('\t' + i)

lastBackup = dirs[len(dirs)-1]
lastBackup = backupDir + '/' + lastBackup

bckp.compareDir(dir2Backup, lastBackup)
input()

areEqual = filecmp.cmp(dir2Backup, lastBackup)

print(areEqual)

if not areEqual:
    dirs = os.listdir(lastBackup)
    print('lastBackup content:')
    for i in dirs:
        print('\t' + i)

for item1 in server_dirs:
        for item2 in dirs:
            if(item1==item2):
                res = filecmp.cmp(lastBackup+'/'+item1, dir2Backup+'/'+item2)
                print(res)
                if not res:
                    mtime1 = os.stat(lastBackup+'/'+item1)
                    mtime1 = mtime1[8]
                    print(mtime1)
                    mtime2 = os.stat(dir2Backup+'/'+item2)
                    mtime2 = mtime2[8]
                    print(mtime2)
                    if (mtime1 > mtime2):
                        print(item1 + ' mas reciente en el servidor')





# https://realpython.com/working-with-files-in-python/
# see dircmp class https://docs.python.org/2/library/filecmp.html
# https://stackoverflow.com/questions/3204782/how-to-check-if-a-file-is-a-directory-or-regular-file-in-python