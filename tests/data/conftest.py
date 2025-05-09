import pytest


@pytest.fixture(scope="function")
def db_session(test_db_url):
    from app.data.db_connect import DataBaseConnect
    db = DataBaseConnect(test_db_url, fill_default_data=False)
    session = db.get_session()
    
    session.begin_nested()
    yield session
    session.rollback()
    session.close()
