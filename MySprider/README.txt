多文件Flask应用结构
|-flasky
  |-app/
    |-templates/
    |-static/
    |-main/
      |-__init__.py
      |-errors.py
      |-forms.py
      |-views.py
    |-__init__.py
    |-email.py
    |-models.py
  |-migrations/
  |-tests/
    |-__init__.py
    |-test*.py
  |-venv/
  |-requirements.txt
  |-config.py
  |-manage.py

结构有四个顶层目录：
    Flask应用一般放置在名为app的目录下。
    migrations目录包含数据库迁移脚本，这和之前说的一样。
    单元测试放置在test目录下
    venv目录包含Python虚拟环境，这和之前说的也是一样的。

一些新的文件：
    requirements.txt列出一些依赖包，这样就可以很容易的在不同的计算机上部署一个相同的虚拟环境。
    config.py存储了一些配置设置。
    manage.py用于启动应用程序和其他应用程序任务。

    应用程序的路由都保存在app/main/views.py模块内部
可以在不同的机器上重新生成虚拟环境
    pip freeze >requirements.txt
当你需要完美复制一个虚拟环境的时候，你可以运行以下命令创建一个新的虚拟环境
    pip install -r requirements.txt