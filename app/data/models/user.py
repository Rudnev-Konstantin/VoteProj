from ..db_connect import Declarative_Base
from flask_login import UserMixin

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy import Integer, String, Text, DateTime

import datetime


class User(Declarative_Base, UserMixin):
    __tablename__ = 'users'
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'user'
    }
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    contests = orm.relationship("Contest", back_populates="author")
    projects = orm.relationship("Project", secondary="users_to_projects", back_populates="authors")
    votes = orm.relationship("Vote", back_populates="voted_user")
    
    # Основные данные
    description = Column(
        Text, nullable=True, 
        comment='Описание пользователя'
    )
    
    # Служебные данные
    created_date = Column(DateTime, default=datetime.datetime.now)


class NormalUser(User):
    __tablename__ = "normal_users"
    __mapper_args__ = {'polymorphic_identity': 'normal_user'}
    
    # Связи и идентификаторы
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    organizations = orm.relationship(
        "Organization", secondary="normal_users_to_organizations",
        back_populates="admins"
    )
    
    # Основные данные
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String, nullable=True)
    avatar_path = Column(
        String, nullable=True,
        default="app/static/images/users/normal/default.jpg",
        comment='Путь к файлу аватарки'
    )
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = orm.relationship("Category", lazy="joined")
    education_id = Column(Integer, ForeignKey('educations.id'))
    education = orm.relationship("Education", lazy="joined")


class Organization(User):
    __tablename__ = "organizations"
    __mapper_args__ = {'polymorphic_identity': 'organization'}
    
    # Связи и идентификаторы
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    admins = orm.relationship(
        "NormalUser", secondary="normal_users_to_organizations",
        back_populates="organizations"
    )
    
    # Основные данные
    title = Column(String)
    illustration_path = Column(
        String, nullable=True,
        default="app/static/images/users/organizations/default.jpg",
        comment='Путь к файлу иллюстрации'
    )


# Статические таблицы
class Education(Declarative_Base):
    __tablename__ = "educations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    education = Column(String)


class Category(Declarative_Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)
