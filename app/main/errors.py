# coding:utf-8
from flask import render_template
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    '''
    功能：禁止访问
    '''

    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    '''

    功能：服务器不存在未找到

    '''

    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    '''

    功能: 内部服务器错误
    
    '''

    return render_template('500.html'), 500
