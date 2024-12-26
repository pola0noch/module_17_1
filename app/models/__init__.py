from app.models.user import User
from app.models.task import Task
from app.backend.db import Base, engine

Base.metadata.create_all(bind=engine)
