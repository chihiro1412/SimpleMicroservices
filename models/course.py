from __future__ import annotations
from pydantic import BaseModel, Field

class Course(BaseModel):
    name: str = Field(description="name of the course")
    department: str = Field(description="department of course, eg. computer science")
    instructor: str = Field(description="prof who teached the class")
    capacity: int = Field(description="max number of students can enroll")
    classroom: str = Field(description="class room of the course")

    model_config = {
        "json_schema_extra": {
            "example": {
              "name": "EECS 183",
              "department": "Computer Science",
              "instructor": "John",
              "capacity": 240,
              "classroom":"BBB136"

            }
        }
    }