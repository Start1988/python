import os

root ='%s%s%s' %('..',os.path.sep,'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Directory: '+ directory)
    for name in subdir_list:
        print ('Subdirectory:' + name)
    for name in file_list:
        print ('File: '+ name)
    print(os.linesep)
