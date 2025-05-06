from ..db_connect import Declarative_Base
from flask_login import UserMixin

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy import Integer, String, Text, DateTime

import datetime


class User(Declarative_Base, UserMixin):
    __tablename__ = 'users'
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = orm.relationship("Category", lazy="joined")
    education_id = Column(Integer, ForeignKey('educations.id'))
    education = orm.relationship("Education", lazy="joined")
    projects = orm.relationship("Project", secondary="users_to_projects", back_populates="users")
    organizations = orm.relationship(
        "Organization", secondary="users_to_organizations",
        back_populates="users"
    )
    votes = orm.relationship("Project_to_Nomination", back_populates="voted_user")
    
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
    __tablename__ = "organizations"
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    users = orm.relationship("User", secondary="users_to_organizations", back_populates="organizations")
    
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


# Статические таблицы
class Education(Declarative_Base):
    __tablename__ = "educations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    education = Column(String)


class Category(Declarative_Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)
