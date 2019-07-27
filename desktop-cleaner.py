import os
import time
import sys
import argparse

parser = argparse.ArgumentParser(description='Moves files and folders from Desktop(or from any other location) to your Documents Folder')
parser.add_argument('number of days', type=str,
                    help='Provide minimum number of days. Example: \"python <script-name> 30\".The script will move files and folders which were created before 30 days.')

args = parser.parse_args()


if sys.argv[1]>str(0):
    hash='#'
    count=0
    dest='C:\\Users\\'+os.environ["USERNAME"]+'\\Documents\\more-than-'+sys.argv[1]+'-days-data\\'
    print(hash*50+'DESKTOP CLEANER'+hash*50)

    if os.path.isdir('C:\\Users\\'+os.environ["USERNAME"]+'\\Documents\\more-than-'+sys.argv[1]+'-days-data')==False:
        print('Creating directory in Documents Folder!')
        os.mkdir('C:\\Users\\'+os.environ["USERNAME"]+'\\Documents\\more-than-'+sys.argv[1]+'-days-data', 0o755)
    else:
        print('Directory already exists!')

    with os.scandir() as dir_entries:
        print('Moving files and folders which were created more than '+sys.argv[1]+' days ago.')
        for entry in dir_entries:
            info = entry.stat()

            time_in_sec = time.time()-(int(sys.argv[1]) * 24 * 60 * 60) # Calcuting time in seconds
            if info.st_ctime<time_in_sec:
                os.rename(entry.path, dest+entry.name)
                count=count+1
        if count!=0:
            print(str(count)+' files/folders moved succesfully!\nAll of them moved to '+dest+'\nThanks for using Desktop Cleaner')
        else:
            print('No file or folder created more than '+sys.argv[1]+' days ago!')


