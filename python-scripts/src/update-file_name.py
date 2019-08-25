import datetime
import os

root = '%s%s%s' % ('..',os.path.sep,'food')
for directory,subdir_list,file_list in os.walk(root):
    for name in file_list:
        source_name = '%s%s%s' %(directory,os.path.sep,name)
        timestamp = os.path.getmtime(source_name)
        print (timestamp)
        print (datetime.datetime.fromtimestamp(timestamp))
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':','.')
        target_name = '%s%s%s_%s' % (directory,os.path.sep,modified_date,name)
        
        print ('Renaming :%s to %s' %(source_name,target_name))

        os.rename(source_name,target_name)
        