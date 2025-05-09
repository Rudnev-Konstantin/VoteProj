import pytest


def test_db_connect_invalid_url():
    with pytest.raises(ValueError):
        from app.data.db_connect import DataBaseConnect
        DataBaseConnect("")


def test_create_tables(db_session):
    from app.data.models.user import User
    result = db_session.query(User).all()
    assert isinstance(result, list)
