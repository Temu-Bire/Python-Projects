from decimal import Decimal
from typing import List

from fastapi import FastAPI
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    computed_field,
    model_validator,
)


class Professor(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    full_name: str = Field(..., min_length=3, max_length=80)
    employee_id: str = Field(..., min_length=7, max_length=7)
    email: EmailStr = Field(...)
    office_room: str | None = None
    teaches_online: bool = False
    salary: Decimal = Field(..., ge=Decimal("15001"))


class Course(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    code: str = Field(..., pattern=r"^[A-Z]{2,4}\d{3,4}$")  # more flexible
    title: str = Field(..., min_length=5, max_length=120)
    credits: int = Field(..., ge=1, le=6)
    semester: str = Field(..., pattern=r"^(Fall|Spring|Summer)$")
    professor_ids: list[str] = Field(default_factory=list)


class Department(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(..., min_length=4, max_length=100)
    code: str = Field(..., pattern=r"^[A-Z]{3,6}$")
    building: str = Field(..., min_length=3, max_length=50)
    head_of_department: Professor
    professors: list[Professor]
    courses: list[Course]
    total_students: int = Field(..., ge=0)

    @computed_field
    @property
    def total_credits_offered(self) -> int:
        return sum(course.credits for course in self.courses)

    @model_validator(mode="after")
    def validate_professor_references(self) -> "Department":
        prof_ids = {p.employee_id for p in self.professors}

        # Check head
        if self.head_of_department.employee_id not in prof_ids:
            raise ValueError(
                f"Head of department ID {self.head_of_department.employee_id!r} "
                "not found in professors list"
            )

        # Check courses
        for course in self.courses:
            for pid in course.professor_ids:
                if pid not in prof_ids:
                    raise ValueError(
                        f"Professor ID {pid!r} in course {course.code!r} "
                        "not found in department professors"
                    )
        return self


app = FastAPI(title="University Departments API")


@app.post("/departments/", response_model=Department)
def create_department(department: Department):
    # computed field is automatically included in response_model
    return department


# For local testing / debugging
if __name__ == "__main__":
    import json

    print("Department JSON Schema:")
    print(json.dumps(Department.model_json_schema(), indent=2))

    # Your sample data here (same as before)
    sample_data = { ... }  # ← paste your dict

    try:
        dept = Department.model_validate(sample_data)
        print("\nValidated successfully!")
        print(dept.model_dump_json(indent=2))
    except Exception as e:
        print("Validation error:", e)

        