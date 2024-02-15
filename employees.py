class Employees:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department


        def setName(self,name):
            self.name = name

        def setAge(self,age):
            self.age = age

        def setId(self,id):
            self.id = id

        def setDep(self,department):
            self.department = department


class EmployeeManagementSystem:
        def __init__(self):
            self.employees = []

        def create_employee(name,age,id,department):
            employee = Employees(name, age, id, department)
            self.employees.append(employee)

        def retrieve_employee(self,id):
            for e in self.employees:
                if e.id ==




def main():
    emp = Employees()

if __name__ == "__main__":
    main()