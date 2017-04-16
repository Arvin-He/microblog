import os
basedir = os.path.abspath(os.path.dirname(__file__))

# 为了激活跨站点请求伪造保护
CSRF_ENABLED = True
# 仅当CSRF激活时才需要,用来建立一个加密令牌,用于验证一个表单
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


# 数据库文件路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# 把SQLAlchemy-migrate数据文件存储在这里
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

