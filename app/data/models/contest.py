from ..db_connect import Declarative_Base

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy import Integer, String, Text, DateTime

import datetime


class Contest(Declarative_Base):
    __tablename__ = "contests"
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = orm.relationship("User", back_populates="contests")
    projects = orm.relationship("Project", secondary="users_to_contests", back_populates="contests")
    nominations = orm.relationship("Nomination", back_populates="contest")
    
    # Основные данные
    title = Column(String)
    illustration_path = Column(
        String, nullable=True,
        default="app/static/images/contests/default.jpg",
        comment='Путь к файлу иллюстрации'
    )
    description = Column(
        Text, nullable=True, 
        comment='Описание конкурса'
    )
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String, nullable=True)
    status_id = Column(Integer, ForeignKey('statuses.id'))
    status = orm.relationship("Status", lazy="joined")
    
    # Служебные данные
    created_date = Column(DateTime, default=datetime.datetime.now)


class Nomination(Declarative_Base):
    __tablename__ = "nominations"
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    contest_id = Column(Integer, ForeignKey('contests.id'))
    contest = orm.relationship("Contest", back_populates="nominations")
    votes = orm.relationship("Vote", back_populates="nomination")
    
    # Основные данные
    title = Column(String)


# Статические таблицы
class Status(Declarative_Base):
    __tablename__ = "statuses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String)
