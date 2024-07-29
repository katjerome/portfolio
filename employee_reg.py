from abc import ABC, abstractmethod

class EmployeeRegistry:
    def __init__(self):
        # Pre-existing employees stored into the dictionary
        self.employees = {
            "Alice Smith": 79686,
            "Tomas Hansen": 56856,
            "Jameson F. Johnson": 54671
        }

    def add_employee(self, first_name, last_name, id_number):
        employee_name = first_name + " " + last_name
        if employee_name in self.employees:
            return "Employee already exists."
        else:
            self.employees[employee_name] = id_number
            return "Employee added successfully."

    def view_all_employees(self):
        return "\n".join(f"Name: {name}, ID: {id}" for name, id in self.employees.items())

    def view_employee_by_id(self, id_number):
        for name, employee_id in self.employees.items():
            if employee_id == id_number:
                return f"Employee details: Name: {name}, ID: {id_number}"
        return "Employee not found."

    def edit_employee(self, employee_name, new_id_number):
        if employee_name in self.employees:
            self.employees[employee_name] = new_id_number
            return "Employee information updated successfully."
        else:
            return "Employee not found."

    def remove_employee(self, employee_name):
        if employee_name in self.employees:
            del self.employees[employee_name]
            return "Employee removed successfully."
        else:
            return "Employee not found."


class Employee(ABC):
    @abstractmethod
    def get_employee_info(self):
        pass

class NewEmployee(Employee):
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def get_employee_info(self):
        return f"{self.first_name} {self.last_name} ID: {self.id_number}"