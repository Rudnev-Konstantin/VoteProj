from ..db_connect import Declarative_Base

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy import Integer


class User_to_Project(Declarative_Base):
    __tablename__ = "users_to_projects"
    
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))


class User_to_Organization(Declarative_Base):
    __tablename__ = "users_to_organizations"
    
    user_id = Column(Integer, ForeignKey('users.id'))
    organization_id = Column(Integer, ForeignKey('organizations.id'))


class Project_to_Contest(Declarative_Base):
    __tablename__ = "users_to_contests"
    
    project_id = Column(Integer, ForeignKey('projects.id'))
    contest_id = Column(Integer, ForeignKey('contests.id'))


class Project_to_Nomination(Declarative_Base):
    __tablename__ = "users_to_nominations"
    
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = orm.relationship("Project", back_populates="nomination_associations")
    nomination_id = Column(Integer, ForeignKey('nominations.id'))
    nomination = orm.relationship("Nomination", back_populates="project_associations")
    voted_user_id = Column(Integer, ForeignKey('users.id'))
    voted_user = orm.relationship("User", back_populates="votes")
