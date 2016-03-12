from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# 工厂函数返回创建的应用程序实例
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
# 蓝图中实现应用程序的功能(一个蓝图就类似于一个可以定义路由的应用程序。不同的是，和路由相关联的蓝图都在休眠状态，只有当蓝图在应用中被注册后，此时的路由才会成为它的一部分。使用定义在全局作用域下的蓝图，定义应用程序的路由就几乎可以和单脚本应用程序一样简单了。)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # attach routes and custom error pages here
    return app