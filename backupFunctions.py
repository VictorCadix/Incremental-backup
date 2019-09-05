import os
import filecmp
import shutil
import datetime
import sys

class backup_struct:
    new = []
    deleted = []
    dir2Backup = ''
    
    def __repr__(self):
        
        print("new :")
        for item in self.new:
            print('\t+' + item)
        
        print("deleted: ")
        for item in self.deleted:
            print('\t-' + item)
        
        return ''

def compareDir (dir_new, dir_old, bckp_struct, verbose=False):
    cmp = filecmp.dircmp(dir_new, dir_old)

    #l_list = cmp.left_list
    #r_list = cmp.right_list

    #print('New:')
    #for item in l_list:
    #    print('\t' + item)

    #print('Old:')
    #for item in r_list:
    #    print('\t' + item)
    
    new = cmp.left_only
    deleted = cmp.right_only

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
        compareDir(dir_new + '/' + folder, dir_old + '/' + folder, bckp_struct)


def generate_incremental_backup(directory, changes_list):

    #Get the name of the folder to backup
    index = changes_list.dir2Backup.rfind("/")
    folder_name = changes_list.dir2Backup[index:]

    #if index < 0:
    #    now = datetime.datetime.now()
    #    date = str(now)[:str(now).find(' ')]
    #else:
    #    date = baseDir[index:]
    #print(date)

    newFolder = directory + '/' + folder_name
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    for dir_name in changes_list.new:
        relative_dir = dir_name.replace(changes_list.dir2Backup, '')
        print(relative_dir)

        if os.path.isfile(dir_name):
            print('is a file')
            path = newFolder + relative_dir
            index = path.rfind('/')
            path = path[:index]
            print(path)
            sys.exit(0)
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy2(dir_name, path)
        else:
            relative_dir = dir_name.replace(changes_list.dir2Backup, '')
            print(relative_dir)
            shutil.copytree(dir_name, newFolder + relative_dir)
    
    f = open(newFolder + '/incremental_bacup.txt','w')
    for dir_name in changes_list.deleted:
        relative_dir = dir_name.replace(changes_list['save_dir'], '')
        f.write('D ' +  relative_dir + '\n')
    f.close()

def build_backup(backup_dir, gen_built_dir):
    backups = os.listdir(backup_dir)
    print('Backup dates:')
    for i in backups:
        print('\t' + i)
    
    newFolder = gen_built_dir + '/' + 'Built'
    #if not os.path.exists(newFolder):
    #    os.makedirs(newFolder)
    
    for i in backups:
        shutil.copy(backup_dir+'/'+i , newFolder)
