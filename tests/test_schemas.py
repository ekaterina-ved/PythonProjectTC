import pytest
from pydantic import ValidationError
from app.schemas import PersonCreate, Person

def test_person_create_schema():
    # Тест валидных данных
    person_data = {"name": "Test User", "age": 30}
    person = PersonCreate(**person_data)
    assert person.name == "Test User"
    assert person.age == 30

def test_person_create_schema_invalid_age():
    # Тест невалидного возраста
    with pytest.raises(ValidationError):
        PersonCreate(name="Test User", age=-1)

def test_person_create_schema_invalid_name():
    # Тест пустого имени
    with pytest.raises(ValidationError):
        PersonCreate(name="", age=30)

def test_person_schema():
    # Тест схемы с ID
    person_data = {"id": 1, "name": "Test User", "age": 30}
    person = Person(**person_data)
    assert person.id == 1
    assert person.name == "Test User"
    assert person.age == 30

def test_person_schema_validation():
    # Тест валидации данных
    with pytest.raises(ValidationError):
        Person(id="not_an_integer", name="Test User", age=30) 