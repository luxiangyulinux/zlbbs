# encoding: utf-8
# config.py by Anderson Huang at 2018/12/24 11:18
import os

"""
配置文件
"""

SECRET_KEY = os.urandom(24)   # 设置随机的SECRET_KEY

# HOSTNAME = '192.168.1.114'  # 链接远程mysql数据库
HOSTNAME = '127.0.0.1'  # 链接本机mysql数据库
PORT = '3306'
DATABASE = 'zlbbs'
USERNAME = 'root'
PASSWORD = '19881214An'
# mysql+pymysql://root:19881214An@192.168.1.114:3306/flask_learn?charset=utf8
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}" \
         "/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD,
                                     host=HOSTNAME, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'ahijdnknj'  # 随意设置cms用户的id字串

# 发送者邮箱的服务器地址和邮箱配置参数，这里使用qq邮箱
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
MAIL_USERNAME = '773985366@qq.com'
MAIL_PASSWORD = 'sjvjkwmovrkzbdge'
MAIL_DEFAULT_SENDER = '773985366@qq.com'
