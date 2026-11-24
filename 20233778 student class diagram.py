class Student:
    def __init__(self, student_id: str, name: str, major: str, gpa: float = 0.0):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa

    @property
    def gpa(self) -> float:
        return self._gpa

    @gpa.setter
    def gpa(self, value: float):
        if 0.0 <= value <= 4.0:
            self._gpa = round(value, 2)
        else:
            raise ValueError("GPA must be between 0.0 and 4.0.")

    def update_gpa(self, new_gpa: float) -> None:
        self.gpa = new_gpa

    def display_info(self) -> None:
        print(f"ID: {self.student_id} | Name: {self.name} | Major: {self.major} | GPA: {self.gpa:.2f}")

    def __str__(self) -> str:
        return f"Student(id='{self.student_id}', name='{self.name}', major='{self.major}', gpa={self.gpa:.2f})"


if __name__ == "__main__":
    student = Student(
        student_id="20233778",
        name="Abubaker nasreldin",
        major="SWE",
        gpa=3.65
    )
    student.display_info()
