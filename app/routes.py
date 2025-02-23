from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

router = APIRouter()

@router.post("/people/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(database.get_db)):
    db_person = models.Person(name=person.name, age=person.age)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

@router.get("/people/", response_model=List[schemas.Person])
def read_people(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    people = db.query(models.Person).offset(skip).limit(limit).all()
    return people

@router.get("/people/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(database.get_db)):
    person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.get("/people/by-age/{age}", response_model=List[schemas.Person])
def get_people_by_age(age: int, db: Session = Depends(database.get_db)):
    people = db.query(models.Person).filter(models.Person.age == age).all()
    return people

@router.get("/people/age-range/", response_model=List[schemas.Person])
def get_people_by_age_range(min_age: int = 0, max_age: int = 150, db: Session = Depends(database.get_db)):
    people = db.query(models.Person)\
        .filter(models.Person.age >= min_age)\
        .filter(models.Person.age <= max_age)\
        .all()
    return people

@router.get("/")
async def root():
    return {"message": "API работает"} 