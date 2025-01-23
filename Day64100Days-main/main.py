class Job:
  def __init__(self, name, salary, hours_worked):
      self.name = name
      self.salary = salary
      self.hours_worked = hours_worked

  def print_details(self):
      print(f"\u2728 Job Type: {self.name} \u2728")
      print(f"   - Salary: {self.salary}")
      print(f"   - Hours Worked: {self.hours_worked}")

class Doctor(Job):
  def __init__(self, name, salary, hours_worked, speciality, years_experience):
      super().__init__(name, salary, hours_worked)
      self.speciality = speciality
      self.years_experience = years_experience

  def print_details(self):
      super().print_details()
      print(f"   - Speciality: {self.speciality}")
      print(f"   - Years of Experience: {self.years_experience}")

class Teacher(Job):
  def __init__(self, name, salary, hours_worked, subject, position):
      super().__init__(name, salary, hours_worked)
      self.subject = subject
      self.position = position

  def print_details(self):
      super().print_details()
      print(f"   - Subject: {self.subject}")
      print(f"   - Position: {self.position}")

# Instantiate the jobs
lawyer = Job("Lawyer", "$ Squillions", 60)
teacher = Teacher("Teacher", "$ Nowhere near enough", "All of them", "Computer Science", "Classroom Teacher")
doctor = Doctor("Doctor", "$ Doing very nicely thank you", 50, "Pediatric Consultant", 7)

# Output the information for each job
print("\n\u2728\u2728\u2728 Jobs Info \u2728\u2728\u2728\n")
lawyer.print_details()
print("\n" + "-" * 30 + "\n")
teacher.print_details()
print("\n" + "-" * 30 + "\n")
doctor.print_details()
