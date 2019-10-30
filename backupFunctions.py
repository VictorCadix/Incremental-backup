import os
import filecmp
import shutil
import datetime
import sys          

class backup_struct:
    
    def __init__(self):
        self.new = []
        self.deleted = []
        self.dir2Backup = ''
        self.baseDir = ''
    
    def __repr__(self):
        
        print("new :")
        for item in self.new:
            print('\t+' + item)
        
        print("deleted: ")
        for item in self.deleted:
            print('\t-' + item)
        
        print() 
        return ''

def check_ignore_list (dir_list, ignore_list):
    i = 0
    for direc in dir_list:
        for ignore_dir in ignore_list:
            if direc == ignore_dir:
                dir_list.remove(i)
            else:
                i += 1

def compareDir (dir_new, dir_old, bckp_struct, ignore_list, verbose=False):
    cmp = filecmp.dircmp(dir_new, dir_old)
    
    new = cmp.left_only
    deleted = cmp.right_only

    check_ignore_list(new, ignore_list)

    if verbose:
        print('New:')
    for item in new:
        bckp_struct.new.append(dir_new + '/' + item)
        if verbose:
            print('\t' + item)

    if verbose:
        print('Deleted:')
    for item in deleted:
        bckp_struct.deleted.append(dir_old + '/' + item)
        if verbose:
            print('\t' + item)
    
    # Compara los archivos con mismo nombre, si son diferentes guarda
    # el que esté en dir_new
    if verbose:
        print('common_files:')
    for item in cmp.common_files:
        if verbose:
            print('\t' + item)
        areEqual = filecmp.cmp(dir_new + '/' + item, dir_old + '/' + item)
        #print('\t\t' + str(areEqual))
        
        if not areEqual:
            bckp_struct.new.append(dir_new + '/' + item)

    # Para directorios comunes utiliza recursión
    if verbose:
        print('common_dirs:')
    for folder in cmp.common_dirs:
        if verbose:
            print('\t' + folder)
        compareDir(dir_new + '/' + folder, dir_old + '/' + folder, bckp_struct, ignore_list)


def generate_incremental_backup(directory, changes_list):

    #Get the name of the folder to backup
    index = changes_list.dir2Backup.rfind('\\')
    folder_name = changes_list.dir2Backup[index:]

    newFolder = directory + folder_name
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    for dir_name in changes_list.new:
        relative_dir = dir_name.replace(changes_list.dir2Backup, '')
        print(relative_dir)

        if os.path.isfile(dir_name):
            print('is a file')
            path = newFolder + relative_dir
            print('1:' + path)
            index = path.rfind('/')
            print('2:' + str(index))
            path = path[:index]
            print('3:' + path)
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy2(dir_name, path)
        else:
            print('Is a folder')
            relative_dir = dir_name.replace(changes_list.dir2Backup, '')
            print(relative_dir)
            shutil.copytree(dir_name, newFolder + relative_dir)
    
    f = open(newFolder + '/incremental_backup.txt','w')
    for dir_name in changes_list.deleted:
        relative_dir = dir_name.replace(changes_list.baseDir, '')
        f.write('D ' +  relative_dir + '\n')
    f.close()

def build_backup(incr_backup_dir, gen_built_dir):
    backups_name = os.listdir(incr_backup_dir)
    print('Backup dates:')
    for bckp_name in backups_name:
        print('\t' + bckp_name)

    while True:
        target_backup = input('Select the backup to build: ')
        if os.path.exists(os.path.join(incr_backup_dir, target_backup)):
            break

    newFolder = gen_built_dir + '/' + 'Built_' + target_backup
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    for bckp_name in backups_name:
        print(bckp_name)

        backup_dir = os.path.join(incr_backup_dir, bckp_name)
        temp_bckp_struct = backup_struct()
        compareDir(backup_dir, newFolder, temp_bckp_struct)
        print(temp_bckp_struct)

        for new in temp_bckp_struct.new:
            
            print('\t' + new)
            name = new[new.rfind('/')+1:]
            relative_path = new.replace(backup_dir,'')
            relative_path = relative_path[:relative_path.rfind('/')]
            if name == 'incremental_backup.txt':
                remove_with_file(new, newFolder)
                continue
            if os.path.isfile(new):
                print('Es file')
                shutil.copy2(new, newFolder + relative_path)
            else:
                print('No es file')
                print(newFolder + relative_path + '/' + name)
                shutil.copytree(new, newFolder + relative_path + '/' + name)
        
        if bckp_name == target_backup:
            # Ha finalizado
            break

def buid_folder(folder_path, gen_built_dir):
    pass

def remove_with_file(file_path, base_dir):
    file = open(file_path, 'r')
    print("Printing the file data:")
    for line in file:
        path2rm = line[2:].replace('\n', '') 
        print (path2rm)
        dir2rm = base_dir + path2rm
        dir2rm = dir2rm.replace('/','\\')
        print("Removing: " + dir2rm)
        if os.path.isfile(dir2rm):      #File
            os.remove(dir2rm)
        if os.path.isdir(dir2rm):       #Folder
            shutil.rmtree(dir2rm)
