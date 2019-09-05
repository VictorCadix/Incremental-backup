import shutil
import os
from pathlib import Path
import backupFunctions as bckp
import sys

while True:
    function_call = input(">>")

    if function_call == 'compare dirs':
        dirA = input("Dir A: ").replace('\"','')
        dirB = input("Dir B: ").replace('\"','')

        bckp_struct = bckp.backup_struct()
        bckp.compareDir(dirA, dirB, bckp_struct)
        print(bckp_struct)
    
    if function_call == 'generate incremental backup':
        dir2Backup = input("Directory to backup: ").replace('\"','')
        base_dir = input('Base directory: ').replace('\"','')
        folder = input('Folder: ').replace('\"','')

        bckp_struct = bckp.backup_struct()
        bckp_struct.new_dir = dir2Backup
        
        bckp.compareDir(dir2Backup, base_dir, bckp_struct)
        bckp.generate_incremental_backup(folder, bckp_struct)
    
    if function_call == 'exit':
        sys.exit(0)
    else:
        print("Unknown command")
        continue


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

#bckp.generate_incremental_backup('C:/Users/victo/Desktop/Incremental Backup', changes_list)

#bckp.build_backup('C:/Users/victo/Desktop/Incremental Backup','C:/Users/victo/Desktop/Incremental Backup')

# https://realpython.com/working-with-files-in-python/
# see dircmp class https://docs.python.org/2/library/filecmp.html
# https://stackoverflow.com/questions/3204782/how-to-check-if-a-file-is-a-directory-or-regular-file-in-python