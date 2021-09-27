from os import getcwd, listdir, rename
import copy

path1 = getcwd()
dirs = listdir(path1)

i = int(input('请输入文件名开始的数字：'))
try:
    b = copy.deepcopy(i)
    for dir in dirs:
        if '.' in dir:
            continue
        rename(str(dir), 'a' + str(b))
        b += 1
    print('第一次批量改名成功')
    input('请按回车，开始第二次改名')
    dirs = listdir(path1)
    for dir in dirs:
        if '.' in dir:
            continue
        rename(str(dir), str(i))
        i += 1
except Exception as ex:
    print(ex)
    input()