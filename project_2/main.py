from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database (for demonstration purposes)
people_db = {}

class Person(BaseModel):
    name: str
    age: int
    email: str

@app.post("/api/", response_model=Person)
def create_person(person: Person):
    if person.name in people_db:
        raise HTTPException(status_code=400, detail="Person already exists")
    people_db[person.name] = person
    return person

@app.get("/api/{user_id}", response_model=Person)
def read_person(user_id: str):
    if user_id not in people_db:
        raise HTTPException(status_code=404, detail="Person not found")
    return people_db[user_id]

@app.put("/api/{user_id}", response_model=Person)
def update_person(user_id: str, updated_person: Person):
    if user_id not in people_db:
        raise HTTPException(status_code=404, detail="Person not found")
    people_db[user_id] = updated_person
    return updated_person

@app.delete("/api/{user_id}", response_model=Person)
def delete_person(user_id: str):
    if user_id not in people_db:
        raise HTTPException(status_code=404, detail="Person not found")
    deleted_person = people_db.pop(user_id)
    return deleted_person
