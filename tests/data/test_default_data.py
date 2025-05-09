def test_fill_default_data(db_session):
    from app.data.default_data import fill_all_default_data
    fill_all_default_data(db_session)
    
    from app.data.models.user import Education
    educations = db_session.query(Education).all()
    assert len(educations) == 6
    
    from app.data.models.user import Category
    categories = db_session.query(Category).all()
    assert len(categories) == 12
    
    from app.data.models.contest import Status
    statuses = db_session.query(Status).all()
    assert len(statuses) == 3


def test_no_duplicates(db_session):
    from app.data.default_data import fill_all_default_data
    fill_all_default_data(db_session)
    fill_all_default_data(db_session)
    
    from app.data.models.user import Education
    educations = db_session.query(Education).all()
    assert len(educations) == 6
