import os
import filecmp
import shutil
import datetime

def compareDir (dir_new, dir_old, changes_list):
    cmp = filecmp.dircmp(dir_new, dir_old)
    l_list = cmp.left_list
    r_list = cmp.right_list

    print('New:')
    for item in l_list:
        print('\t' + item)

    print('Old:')
    for item in r_list:
        print('\t' + item)
    
    new = cmp.left_only
    deleted = cmp.right_only

    print('New:')
    for item in new:
        changes_list['new'].append(dir_new + '/' + item)
        print('\t' + item)

    print('Deleted:')
    for item in deleted:
        changes_list['deleted'].append(dir_old + '/' + item)
        print('\t' + item)
    
    # Compara los archivos con mismo nombre, si son diferentes guarda
    # el que esté en dir_new
    print('common_files:')
    for item in cmp.common_files:
        print('\t' + item)
        areEqual = filecmp.cmp(dir_new + '/' + item, dir_old + '/' + item)
        #print('\t\t' + str(areEqual))
        
        if not areEqual:
            changes_list['new'].append(dir_new + '/' + item)

    # Para directorios comunes utiliza recursión
    print('common_dirs:')
    for folder in cmp.common_dirs:
        print('\t' + folder)
        compareDir(dir_new + '/' + folder, dir_old + '/' + folder, changes_list)


def generate_incremental_backup(directory, changes_list):
    baseDir = changes_list['updated_dir']
    index = baseDir.find("20")
    if index < 0:
        now = datetime.datetime.now()
        date = str(now)[:str(now).find(' ')]
    else:
        date = baseDir[index:]
    print(date)

    newFolder = directory + '/' + date
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    for dir_name in changes_list['new']:
        relative_dir = dir_name.replace(changes_list['updated_dir'], '')
        print(relative_dir)

        if os.path.isfile(dir_name):
            print('is a file')
            path = newFolder + relative_dir
            index = path.rfind('/')
            path = path[:index]
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy2(dir_name, path)
        else:
            relative_dir = dir_name.replace(changes_list['updated_dir'], '')
            print(relative_dir)
            shutil.copytree(dir_name, newFolder + relative_dir)
    
