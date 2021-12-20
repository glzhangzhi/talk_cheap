OS目录操作方法

```python
os.mkdir('dir') # 创建目录
os.makedirs('a/dirs')  # 递归的创建目录
shutil.copyfile('oldfile', 'newfile') # 复制文件
shutil.copy('oldpath', 'newfile or target dir') # 复制文件或目录
shutil.copytree('olddir', 'new and noexist dir') # 复制目录
os.rename('oldname', 'newname') # 重命名文件或目录
shutil.move('old dir', 'new dir') # 移动文件或目录
os.remove('file') # 删除文件
os.rmdir('empty dir') #删除目录
os.listdir('dir') # 列出目录下所有文件名和目录名
os.path.split('path') # 分隔目录名和文件名
os.getcwd() # 获取当前工作目录
os.path.dirname() # 获取路径名
os.path.basename() # 获取文件名
os.path.exists('path') # 给定目录是否存在
os.system('commend') # 运行shell命令
```