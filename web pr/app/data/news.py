import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
  # image = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    city=sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    type=sqlalchemy.Column(sqlalchemy.String,nullable=True)
    room = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    categories = orm.relation("Category", secondary="association", backref="news")