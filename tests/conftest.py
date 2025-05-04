import pytest

from app import create_app
# from app.data.models. import model
# ...


@pytest.fixture
def client():
    # Создаём временную БД в памяти
    app = create_app("testing", db_cone_url="sqlite:///:memory:")
    
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
