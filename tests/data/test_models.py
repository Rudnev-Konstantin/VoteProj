from datetime import datetime


def test_user_model(db_session):
    from app.data.models.user import User
    user = User(description="Test user")
    
    db_session.add(user)
    db_session.commit()
    
    assert user.id is not None
    assert isinstance(user.created_date, datetime)


def test_normal_user_inheritance(db_session):
    from app.data.models.user import NormalUser, User
    user = NormalUser(
        name="John",
        surname="Doe",
        education_id=1,
        category_id=1
    )
    
    db_session.add(user)
    db_session.commit()
    
    assert isinstance(user, User)
    assert user.type == "normal_user"


def test_contest_relationships(db_session):
    from app.data.models.contest import Contest
    from app.data.models.user import User
    user = User(description="Organizer")
    contest = Contest(
        title="Test Contest",
        author=user,
        start_date=datetime.now(),
        end_date=datetime.now(),
        status_id=1
    )
    
    db_session.add_all([user, contest])
    db_session.commit()
    
    assert len(user.contests) == 1
    assert user.contests[0].title == "Test Contest"
    assert contest.author.description == "Organizer"
