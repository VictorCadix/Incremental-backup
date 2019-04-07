import filecmp

def compareDir (dir_new, dir_old):
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
        print('\t' + item)

    print('Deleted:')
    for item in deleted:
        print('\t' + item)
    
    #cmp.common_dirs
    #cmp.common_files

    # Para directorios comunes utiliza recursión
    print('common_dirs:')
    for folder_name in cmp.common_dirs:
        print('\t' + folder_name)
        compareDir(dir_new + '/' + folder_name, dir_old + '/' + folder_name)

    print('common_files:')
    for item in cmp.common_files:
        print('\t' + item)
        
        # Compara los archivos con mismo nombre, si son diferentes guarda
        # el que esté en dir_new
        areEqual = filecmp.cmp(dir_new+'/'+item, dir_old+'/'+item)
        print('\t\t' + str(areEqual))