import pytest

from app import create_app
# from app.data.models. import model
# ...


@pytest.fixture(scope="session")
def test_db_url():
    return "sqlite:///:memory:"


@pytest.fixture(scope="function")
def client(test_db_url):
    app = create_app("testing", db_cone_url=test_db_url)
    
    with app.app_context():
        with app.db_connect.get_session() as session:
            # test_data
            # ...
            
            data = []
            # data = [test_data_1, *test_data_n]
            
            session.add_all(data)
            session.commit()
        
        session.begin_nested()
        yield app.test_client()
        session.rollback()
        session.close()
