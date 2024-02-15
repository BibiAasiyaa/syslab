class Employees:
    def __init__(self, name, age, e_id, department):
        self.name = name
        self.age = age
        self.e_id = e_id
        self.department = department


    def setName(self,name):
        self.name = name

    def setAge(self,age):
        self.age = age

    def setId(self,e_id):
        self.e_id = e_id

    def setDep(self,department):
        self.department = department


class EmployeeManagementSystem:
        def __init__(self):
            self.employees = []

        def create_employee(self, name,age,e_id,department):
            employee = Employees(name, age, e_id, department)
            self.employees.append(employee)

        def retrieve_employee(self,e_id):
            for e in self.employees:
                if e.e_id == e_id:
                    return e
            return None
        
        def delete_employee(self,e_id):
            for e in self.employees:
                if e.e_id == e_id:
                    self.employees.remove(e)
                    return True
            return False


'''def main():
    emp = Employees()

if __name__ == "__main__":
    main()
'''