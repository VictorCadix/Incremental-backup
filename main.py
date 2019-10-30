import shutil
import os
from pathlib import Path
import backupFunctions as bckp
import sys

while True:
    function_call = input(">> ")

    if function_call == 'compare dirs':
        dirA = input("Dir A: ").replace('\"','')
        dirB = input("Dir B: ").replace('\"','')

        bckp_struct = bckp.backup_struct()
        ignore_list = bckp.load_ignore_list()
        bckp.compareDir(dirA, dirB, bckp_struct, ignore_list)
        print(bckp_struct)
    
    elif function_call == 'generate incremental backup':
        dir2Backup = input("Directory to backup: ").replace('\"','')
        base_dir = input('Base directory: ').replace('\"','')
        folder = input('Folder: ').replace('\"','')

        bckp_struct = bckp.backup_struct()
        bckp_struct.dir2Backup = dir2Backup
        bckp_struct.baseDir = base_dir
        
        bckp.compareDir(dir2Backup, base_dir, bckp_struct)
        bckp.generate_incremental_backup(folder, bckp_struct)

    elif function_call == 'build backup':
        incr_bckp_dir = input('Incremental backup dir: ').replace('\"','')
        gen_dir = input('Save built directory: ').replace('\"','')
        bckp.build_backup(incr_bckp_dir, gen_dir)
    
    elif function_call == 'exit':
        sys.exit(0)
    else:
        print("Unknown command")
        continue