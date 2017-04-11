# coding:utf-8
from flask import Blueprint

auth = Blueprint('auth', __name__)#注册登录蓝本

from . import views
