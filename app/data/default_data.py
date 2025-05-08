from models.user import Education, Category
from models.contest import Status


def fill_educations(session):
    default_educations = [
        "1 курс Яндекс Лицея",
        "2 курс Яндекс Лицея",
        "Школьная программа",
        "Программа Колледжа",
        "Программа ВУЗ(а)",
        "Другое..."
    ]
    
    with session as session:
        existing = {education.education for education in session.query(Education).all()}
        to_add = [
            Education(education=education) for education in default_educations 
            if education not in existing
        ]
        
        if to_add:
            session.add_all(to_add)
            session.commit()


def fill_categories(session):
    default_categories = [
        "7 класс",
        "8 класс",
        "9 класс",
        "10 класс",
        "11 класс",
        "1 курс",
        "2 курс",
        "3 курс",
        "4 курс",
        "5 курс",
        "Работа...",
        "Другое..."
    ]
    
    with session as session:
        existing = {category.category for category in session.query(Category).all()}
        to_add = [
            Category(category=category) for category in default_categories 
            if category not in existing
        ]
        
        if to_add:
            session.add_all(to_add)
            session.commit()


def fill_statuses(session):
    default_statuses = [
        "Набор кандидатов",
        "Проходит...",
        "Завершено"
    ]
    
    with session as session:
        existing = {status.status for status in session.query(Status).all()}
        to_add = [
            Status(status=status) for status in default_statuses 
            if status not in existing
        ]
        
        if to_add:
            session.add_all(to_add)
            session.commit()


def fill_all_default_data(session):
    fill_educations(session)
    fill_categories(session)
    fill_statuses(session)
