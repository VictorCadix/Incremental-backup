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