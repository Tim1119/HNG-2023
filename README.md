# HNG PROJECT 2 (2023)
This is my github for hng 2023

##Project 2

#  Documentation
This documentation provides information on how to use my FastAPI CRUD API for managing people's resources

## Endpoints

### 1. Create a Person

- **Endpoint**: `POST /api/`
- **Request Format**:
  ```json
  {
    "name": "string",
    "age": integer,
    "email": "string"
  }
- **Response Format**:
  ```json
  {
    "name": "string",
    "age": integer,
    "email": "string"
  }

### 2. Read a Person

- **Endpoint**: `GET /api/{user_id}`
- **Response Format**:
  ```json
  {
  "name": "string",
  "age": integer,
  "email": "string"
  }

### 3. Update a Person

- **Endpoint**: `PUT /api/{user_id}`
- **Request Format**:
  ```json
  {
  "name": "string",
  "age": integer,
  "email": "string"
}
- **Response Format**:
  ```json
 {
  "name": "string",
  "age": integer,
  "email": "string"
}

### 4. Delete a Person

- **Endpoint**: `DELETE /api/{user_id}`
- **Response Format**:
  ```json
  {
  "name": "string",
  "age": integer,
  "email": "string"
}

# Sample Usage

## Create a Person
### Request:
curl -X POST -d '{"name": "Femi Falana", "age": 25, "email": "femifalana@example.com"}' http://localhost:8000/api/
### Response
{
  "name": "Femi Falana",
  "age": 25,
  "email": "femifalana@example.com"
}

## Read a Person
### Request:
curl http://localhost:8000/api/Femi%20Falana
### Response
{
  "name": "Femi Falana",
  "age": 25,
  "email": "femifalana@example.com"
}

## Update a Person
### Request:
curl -X PUT -d '{"name": "Femi Falana", "age": 26, "email": "femi.falana@example.com"}' http://localhost:8000/api/Femi%20Falana
### Response
{
  "name": "Femi Falana",
  "age": 26,
  "email": "femi.falana@example.com"
}

## Delete a Person
### Request:
curl -X PUT -d '{"name": "Femi Falana", "age": 26, "email": "femi.falana@example.com"}' http://localhost:8000/api/Femi%20Falana
### Response
{
  "name": "John Doe",
  "age": 26,
  "email": "john.doe@example.com"
}



## Known Limitations and Assumptions
*The API assumes that the name field is unique, and it uses the name as the identifier for CRUD operations.
*Security features, such as authentication and authorization, are not implemented in this project.

## Setup and Deployment
- Clone the project to your local computer using *git clone [url]* command
- create a virtual enviroment with python using *python -m venv [name of enviroment]* or *python3 -m venv [name of enviroment]* e.g. venv,env
- activate the virtual env using *venv/scripts/activate*
- then run *pip install requirements.txt*
- Lastly run *uvicorn main:app --reload* to start the server


