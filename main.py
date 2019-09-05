import shutil
import os
from pathlib import Path
import filecmp
import backupFunctions as bckp

bckp_struct = bckp.backup_struct()
dir2Backup = "C:/Users/victo/Desktop/Server"
save_dir = "C:/Users/victo/Desktop/BackupServer/2019-04-08"

""" server_dirs = os.listdir(dir2Backup)
print('folderContent')
for i in server_dirs:
    print('\t' + i)


dirs = os.listdir(save_dir)
print('Destination files:')
for i in dirs:
    print('\t' + i) """

#lastBackup = dirs[len(dirs)-1]
#lastBackup = dest_dir + '/' + lastBackup

bckp.compareDir(dir2Backup, save_dir, bckp_struct)
print(bckp_struct)

#bckp.generate_incremental_backup('C:/Users/victo/Desktop/Incremental Backup', changes_list)

#bckp.build_backup('C:/Users/victo/Desktop/Incremental Backup','C:/Users/victo/Desktop/Incremental Backup')

# https://realpython.com/working-with-files-in-python/
# see dircmp class https://docs.python.org/2/library/filecmp.html
# https://stackoverflow.com/questions/3204782/how-to-check-if-a-file-is-a-directory-or-regular-file-in-python