import filecmp

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
        changes_list['deleted'].append(dir_new + '/' + item)
        print('\t' + item)
    
    # Compara los archivos con mismo nombre, si son diferentes guarda
    # el que esté en dir_new
    print('common_files:')
    for item in cmp.common_files:
        print('\t' + item)
        areEqual = filecmp.cmp(dir_new + '/' + item, dir_old + '/' + item)
        print('\t\t' + str(areEqual))
        
        if not areEqual:
            changes_list['new'].append(dir_new + '/' + item)

    # Para directorios comunes utiliza recursión
    print('common_dirs:')
    for folder in cmp.common_dirs:
        print('\t' + folder)
        compareDir(dir_new + '/' + folder, dir_old + '/' + folder, changes_list)
        