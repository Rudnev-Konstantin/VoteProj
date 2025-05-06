from ..db_connect import Declarative_Base

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy import Integer, String, Text, DateTime

import datetime


class Contest(Declarative_Base):
    __tablename__ = "contests"
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_id = Column(Integer, ForeignKey('statuses.id'))
    status = orm.relationship("Status", lazy="joined")
    
    # Основные данные
    title = Column(String)
    illustration_path = Column(
        String, nullable=True,
        comment='Путь к файлу иллюстрации'
    )
    description = Column(
        Text, nullable=True, 
        comment='Описание конкурса'
    )
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String, nullable=True)
    
    # Служебные данные
    created_date = Column(DateTime, default=datetime.datetime.now)


class Nomination(Declarative_Base):
    __tablename__ = "nominations"
    
    # Связи и идентификаторы
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Основные данные
    title = Column(String)


# Статические таблицы
class Status(Declarative_Base):
    __tablename__ = "statuses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String)
