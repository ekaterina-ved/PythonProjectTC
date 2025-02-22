import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.database import Base, get_db
from app.models import Person

@pytest.fixture(autouse=True)
def setup_database():
    # Создаем тестовую БД в памяти
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False}
    )
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    
    yield
    
    # Очищаем после тестов
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def test_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    
    with Session(engine) as session:
        yield session

def test_create_person(test_db):
    # Тест создания записи в БД
    person = Person(name="Test User", age=30)
    test_db.add(person)
    test_db.commit()
    
    assert person.id is not None
    
    # Проверяем, что запись действительно создалась
    db_person = test_db.query(Person).first()
    assert db_person.name == "Test User"
    assert db_person.age == 30

def test_get_db():
    # Тест генератора сессий БД
    db = next(get_db())
    assert isinstance(db, Session)
    db.close()