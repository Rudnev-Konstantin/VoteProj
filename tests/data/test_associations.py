def test_association(db_session):
    from app.data.models.user import User
    from app.data.models.project import Project
    
    user_1 = User(description="Test User_1")
    user_2 = User(description="Test User_2")
    project_1 = Project(title="Test Project_1")
    project_2 = Project(title="Test Project_2")
    
    user_1.projects.append(project_1)
    user_1.projects.append(project_2)
    project_1.authors.append(user_2)
    
    db_session.add_all([user_1, user_2, project_1])
    db_session.commit()
    
    assert len(user_1.projects) == 2
    assert len(project_1.authors) == 2
    assert len(user_2.projects) == 1
    assert len(project_2.authors) == 1
    assert user_2.projects[0] in user_1.projects


def test_normal_user_organization(db_session):
    from app.data.models.user import NormalUser
    from app.data.models.user import Organization
    
    normal_user = NormalUser(description="Test NormalUser")
    organization = Organization(description="Test Organization")
    
    normal_user.organizations.append(organization)
    
    db_session.add_all([normal_user, organization])
    db_session.commit()
    
    assert len(normal_user.organizations) == 1
    assert len(organization.admins) == 1
    assert organization.admins[0].description == "Test NormalUser"


def test_vote_relationships(db_session):
    from app.data.models.contest import Nomination
    from app.data.models.project import Project
    from app.data.models.user import User
    from app.data.models.associations import Vote
    
    user = User(description="Voter")
    project = Project(title="Project")
    nomination = Nomination(title="Best Project")
    vote = Vote(
        voted_user=user,
        project=project,
        nomination=nomination
    )
    
    user.votes.append(vote)
    
    db_session.add_all([user, project, nomination, vote])
    db_session.commit()
    
    assert len(user.votes) == 1
    assert len(project.votes) == 1
    assert len(nomination.votes) == 1
    assert vote.nomination.title == "Best Project"
