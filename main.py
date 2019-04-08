import shutil
import os
from pathlib import Path
import filecmp
import backupFunctions as bckp

dir2Backup = "C:/Users/victo/Desktop/Server"
backupDir = "C:/Users/victo/Desktop/BackupServer/2019-04-07"

new = []
deleted = []
changes_list = {}
changes_list['new'] = new
changes_list['deleted'] = deleted
changes_list['updated_dir'] = ''
changes_list['save_dir'] = ''


server_dirs = os.listdir(dir2Backup)
print('folderContent')
for i in server_dirs:
    print('\t' + i)


dirs = os.listdir(backupDir)
print('Destination files:')
for i in dirs:
    print('\t' + i)

#lastBackup = dirs[len(dirs)-1]
#lastBackup = backupDir + '/' + lastBackup

changes_list['updated_dir'] = dir2Backup
changes_list['save_dir'] = backupDir

bckp.compareDir(dir2Backup, backupDir, changes_list)
print(changes_list)

bckp.generate_incremental_backup('C:/Users/victo/Desktop/Incremental Backup', changes_list)

bckp.build_backup('C:/Users/victo/Desktop/Incremental Backup','C:/Users/victo/Desktop/Incremental Backup')

# https://realpython.com/working-with-files-in-python/
# see dircmp class https://docs.python.org/2/library/filecmp.html
# https://stackoverflow.com/questions/3204782/how-to-check-if-a-file-is-a-directory-or-regular-file-in-python