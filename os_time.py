import os
import time
print('a')
print(os.getcwd())

os.mkdir('nowy_folder')

time.sleep(5)

os.rename('nowy_folder', 'nowy_folder_2')
time.sleep(5)
os.rmdir('nowy_folder_2')