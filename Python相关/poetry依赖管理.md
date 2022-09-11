Poetry是一个Python依赖管理和打包工具，用来声明项目所依赖的库并且管理（安装/更新）他们。它使用lockfile来保证可重复的安装，并能在不同的分发环境构建你的项目。

# 系统需求

Python 3.7+

# 安装

## Linux，macOS，WSL

`curl -sSL https://install.python-poetry.org | python -`

## Windows Powershell

`(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

# 设定系统路径

一般在安装时，Poetry会把库添加到系统路径中，也可以手动添加

`~/Library/Application Support/pypoetry/bin/poetry` on MacOS
`~/.local/share/pypoetry/bin/poetry` on Linux/Unix
`%APPDATA%\pypoetry\Scripts\poetry` on Windows

# 新建项目

`poetry new project-demo`

这将会在当前目录新建一个项目文件夹project-demo，其结构如下

```
project-demo
|--pyproject.toml
|--README.md
|--project-demo
|  |--__init__.py
|--tests
   |--__init__.py
```

其中最重要的文件就是`pyproject.toml`，其内容如下

```
[tool.poetry]
name = "project-demo"
version = "0.1.0"
description = ""
authors = ["Test <Test@Test.de>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

# 在一个已经存在的项目中安装poetry

切换到项目文件夹中，使用`poetry init`命令，会开始一个交互式的创建过程

# 指定依赖

你可以在toml文件中直接指定项目中用到的依赖项

```
[tool.poetry.dependencies]
pendulum = "^2.1"
```

或者使用`poetry add pendulum`来添加依赖，效果与更改toml文件类似

# 创建、运行和激活虚拟环境

默认配置下，poetry会在`{cache-dir}/virtualenvs`目录下创建一个项目对应的虚拟环境，你可以通过指定文件中的`cache-dir`项来设置缓存目录，或在命令行中使用`poetry config virtualenvs.in-project true`来设置是否在项目文件夹中创建虚拟环境

简单的使用`poetry run python your_script.py`或`poetry run pytest`来在该虚拟环境中运行你的脚本

使用`poetry shell`来新建一个该虚拟环境下的shell

# 指定版本约束

在toml文件中记录的依赖库版本约束，符合以下规则：

| 依赖描述 | 允许的版本范围 |
| -------- | -------------- |
| ^1.2.3   | >=1.2.3 <2.0.0 |
| ^1.2     | >=1.2 < 2      |
| ^1       | >=1 <2         |
| ^0.2.3   | >=0.2.3 < 0.3  |
| ^0.0.3   | >=0.0.3 <0.4   |

可以看到，poetry会搜索在满足 [不修改最左边第一个非零版本号] 前提下的最新的版本

# 安装依赖

使用`poetry install`来安装项目中的依赖，这会有两种情况：

## 1. installing without poetry.lock

如果你之前从没运行过这个命令，且你的库中没有poetry.lock这个文件，那么poetry会解析pyproject.toml文件中的所有依赖并安装他们的最新版。之后，poetry会将所有库和他们的版本写入poetry.lock文件中，将项目依赖锁定到指定的版本。你应该将你的poetry.lock文件纳入你的版本控制和repo中，以便其他使用这个项目的人拥有相同的版本依赖。

## 2. installing with poetry.lock

如果在运行install命令前，你的项目中已经有了poetry.lock和pyproject.toml文件，这意味着你之前曾经运行过这个命令，或者其他管理这个库的人运行了并且将他们纳入了版本控制中。此时，再执行install命令，poetry会按照poetry.lock中的版本显示来索引pyproject.toml中的依赖库，所以此时安装的不一定是最新的版本，但一定是符合项目依赖的版本。

# 构建项目

`poetry build`

# 发布到PyPI

`poetry publish`

`poetry --build publish`

# 管理虚拟环境

默认情况下，poetry会检查当前当前是否在虚拟环境中运行，如果是，它将直接使用它，否则，它会尝试使用安装poetry的python版本来创建一个虚拟环境。如果你想在你的项目中使用不同的python版本，请在你使用的虚拟环境工具（例如conda或pipenv）中创建并激活一个，然后再尝试`poetry install`。

# 指定使用的虚拟环境

```
poetry env use /full/path/to/python
```

# 显示当前环境信息

```
poetry env info
```

它会显示当前激活的虚拟环境的信息

```
Virtual environment
Python:         3.7.1
Implementation: CPython
Path:           /path/to/poetry/cache/virtualenvs/test-O3eWbxRl-py3.7
Valid:          True

System
Platform: darwin
OS:       posix
Python:   /path/to/main/python
```

# 显示与当前项目关联的虚拟环境

```
poetry env list
poetry env list --full-path
```

# 删除虚拟环境

```
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7
poetry env remove --all
```

