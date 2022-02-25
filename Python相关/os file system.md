```python
os.mkdir('dir') # make dir
os.makedirs('a/dirs')  # mkdir recursive

shutil.copyfile('oldfile', 'newfile') # copy file
shutil.copy('oldpath', 'newfile or target dir') # copy file or directory
shutil.copytree('olddir', 'new and noexist dir') # copy directory

os.rename('oldname', 'newname') # rename file or directory
shutil.move('old dir', 'new dir') # move file or directory

os.remove('file') # delete file
os.rmdir('empty dir') # delete directory

os.listdir('dir') # list file and directory
os.getcwd() # get the current working directory

os.system('commend') # run shell command

# it is better to use pathlib than os.path
os.path.split('path')
os.path.dirname()
os.path.basename()
os.path.exists('path')
```