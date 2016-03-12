from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
# 一个蓝图就类似于一个可以定义路由的应用程序。不同的是，和路由相关联的蓝图都在休眠状态，只有当蓝图在应用中被注册后，此时的路由才会成为它的一部分。使用定义在全局作用域下的蓝图，定义应用程序的路由就几乎可以和单脚本应用程序一样简单了。
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors