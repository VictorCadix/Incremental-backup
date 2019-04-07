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




# https://realpython.com/working-with-files-in-python/
# see dircmp class https://docs.python.org/2/library/filecmp.html
# https://stackoverflow.com/questions/3204782/how-to-check-if-a-file-is-a-directory-or-regular-file-in-python