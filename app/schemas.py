from pydantic import BaseModel, Field, ConfigDict

class PersonBase(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, le=150, description="Возраст человека (от 0 до 150 лет)")

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True) 