from ..db_connect import Declarative_Base

from sqlalchemy import Column, orm
from sqlalchemy import Integer, String, Text, DateTime

import datetime


class Project(Declarative_Base):
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
        comment='Описание проекта'
    )
    video_path = Column(
        String, nullable=True,
        comment='Путь к файлу видео'
    )
    resource_url = Column(
        String, nullable=True,
        comment='url ресурса, на котором размещён проект'
    )
    
    # Служебные данные
    created_date = Column(DateTime, default=datetime.datetime.now)
