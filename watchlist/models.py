from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from watchlist import app, db
class User(db.Model, UserMixin):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    username = db.Column(db.String(20))  # 登录用户名
    password_hash = db.Column(db.String(60))  # 密码散列值

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # 对密码进行哈希

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # 对比哈希的密码值


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份

