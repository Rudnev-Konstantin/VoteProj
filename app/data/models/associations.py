from ..db_connect import Declarative_Base

from sqlalchemy import Table, Column, ForeignKey, orm
from sqlalchemy import Integer


User_to_Project = Table(
    "users_to_projects",
    Declarative_Base.metadata,
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("project_id", Integer, ForeignKey('projects.id'))
)


NormalUsers_to_Organization = Table(
    "normal_users_to_organizations",
    Declarative_Base.metadata,
    Column("normal_user_id", Integer, ForeignKey('normal_users.id')),
    Column("organization_id", Integer, ForeignKey('organizations.id'))
)


Project_to_Contest = Table(
    "users_to_contests",
    Declarative_Base.metadata,
    Column("project_id", Integer, ForeignKey('projects.id')),
    Column("contest_id", Integer, ForeignKey('contests.id'))
)


class Vote(Declarative_Base):
    __tablename__ = "votes"
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = orm.relationship("Project", back_populates="votes")
    nomination_id = Column(Integer, ForeignKey('nominations.id'))
    nomination = orm.relationship("Nomination", back_populates="votes")
    voted_user_id = Column(Integer, ForeignKey('users.id'))
    voted_user = orm.relationship("User", back_populates="votes")
