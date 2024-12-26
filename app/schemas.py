from pydantic import BaseModel

class CreateUser:
    username : str
    firstname : str
    lastname : str
    age : int

class UpdateUser:
    username : str
    firstname: str
    lastname: str
    age: int

class CreateTask:
    title : str
    content : str
    priority : int

class UpdateTask:
    title: str
    content: str
    priority: int

