import pytest
from app.models import Person
from app.schemas import PersonCreate, Person as PersonSchema

def test_person_model():
    # Тест создания модели Person
    person = Person(name="Test User", age=30)
    assert person.name == "Test User"
    assert person.age == 30
    assert person.id is None  # ID должен быть None до сохранения в БД

def test_person_model_repr():
    # Тест строкового представления модели
    person = Person(name="Test User", age=30)
    assert str(person) == f"Person(name='Test User', age=30)"

def test_person_model_properties():
    # Тест свойств модели
    person = Person(name="Test User", age=30)
    assert hasattr(person, 'name')
    assert hasattr(person, 'age')
    assert hasattr(person, 'id') 