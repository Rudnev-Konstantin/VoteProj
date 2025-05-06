from ..db_connect import Declarative_Base
from flask_login import UserMixin

from sqlalchemy import Column, orm
from sqlalchemy import Integer, String, Text, DateTime

import datetime


class User(Declarative_Base, UserMixin):
    __tablename__ = 'users'
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Основные данные
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String, nullable=True)
    avatar_path = Column(
        String, nullable=True,
        comment='Путь к файлу аватарки'
    )
    description = Column(
        Text, nullable=True, 
        comment='Описание пользователя'
    )
    
    # Служебные данные
    created_date = Column(DateTime, default=datetime.datetime.now)


class Organization(Declarative_Base, UserMixin):
    __tablename__ = "projects"
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Основные данные
    title = Column(String)
    illustration_path = Column(
        String, nullable=True,
        comment='Путь к файлу иллюстрации'
    )
    description = Column(
        Text, nullable=True, 
        comment='Описание организации'
    )
    
    # Служебные данные
    created_date = Column(DateTime, default=datetime.datetime.now)
