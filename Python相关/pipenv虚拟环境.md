[TOC]

# 安装
pip install pipenv

# 显示目前的环境目录

pipenv --venv

# 创建环境

pipenv install --three
--three代表以python3为基础

# 启动环境

pipenv shell

# 安装第三方库

pipenv install requests
pipenv install --dev requests  # 安装为开发环境

# 退出环境

exit

# 查看解释器目录

pipenv --py

# 查看包依赖关系

pipenv graph

# 卸载第三方库

pipenv uninstall requests
pipenv uninstall --all  # 删除所有第三方库

# 在虚拟环境下运行脚本
pipenv run python test.py

# 删除环境

pipenv --rm
会在C:\Users\glzha\\.virtualenvs\这个目录下生成虚拟环境相关配置文件







# pipenv Options:

--where  项目本地路径信息
--venv  虚拟环境信息
--py  Python解释器信息
--envs  环境变量选项
--rm  移除虚拟环境
--bare  最小化输出
--completion  完整显示信息
--man  手册
--support  在Github中的诊断信息
--site-packages / --no-site-packages  
--python 指定虚拟环境使用的python版本
--three / --two  使用pyton3/2创建环境
--clear  清除缓存(pipenv, pip, pip-tools)
\-v / --verbose  详细显示模式
--pypi-mirror TEXT  指定PyPI镜像
-h / --help  显示帮助信息
--dev  在开发环境中安装包
\-r 导入requirements.txt

# pipenv Commands:

check  检查安全性
clean  清除所有没在Pipfile.lock里指定的包
graph  显示已安装的依赖图信息
install  安装指定的包，如果没有指定，则安装所有在Pipfile中的包
lock  生成Pipfile.lock
run  运行安装在虚拟环境中的命令，即是pipenv run python xxx.py
scripts  列出在当前环境配置中的scripts
shell  在一个虚拟环境中生成一个shell，相当于进入环境
sync  安装所有在Pipfile.lock中指定的包
uninstall  卸载指定的包并将其从Pipfile中移除
update  先运行lock，再运行sync

