from typing import List
from __future__ import annotations
from pydantic import BaseModel, Field
from .course import Course

class Student(BaseModel):
    first_name: str = Field(description="First name of student")
    last_name: str = Field(description="Last name of student")
    gender: str = Field(description="Gender of student")
    student_id: int = Field(description="Numeric value, can uniquely identify student,4 digit long")
    major: str = Field(description="Major name")
    year: int = Field(description="Value from freshman, sophomore, junior, senior")
    courses: List[Course] = Field(
        default_factory=list,
        description="Courses linked to student",
        json_schema_extra={
            "example": [
                {
              "name": "EECS 183",
              "department": "Computer Science",
              "instructor": "John",
              "capacity": 240,
              "classroom":"BBB136"
                }
            ]
        },
    )
   
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name":"Rocco",
                    "last_name": "Lampone",
                    "gender": "male",
                    "student_id": 1234,
                    "major": "Mechanic Engineering",
                    "year": "freshman",
                    "courses": [
                                {
                        "name": "EECS 183",
                        "department": "Computer Science",
                        "instructor": "John",
                        "capacity": 240,
                        "classroom":"BBB136"

                        }
                    ],
                }
            ]
        }
    }